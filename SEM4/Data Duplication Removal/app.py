from flask import Flask, request, render_template, send_from_directory, url_for
import zipfile
import os
import hashlib
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
EXTRACT_FOLDER = "extracted"
OUTPUT_ZIP_FOLDER = "output_zip"
STATIC_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXTRACT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_ZIP_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

def list_main_zip_contents(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()
        valid_files = [os.path.basename(f) for f in all_files
                       if not f.startswith('__MACOSX/')
                       and not f.endswith('/')
                       and not os.path.basename(f).startswith('._')
                       and os.path.basename(f) != '.DS_Store'
                       and os.path.basename(f)]
        return sorted(set(valid_files))

def extract_unique_files(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()
        valid_files = [f for f in all_files
                       if not f.startswith('__MACOSX/')
                       and not f.endswith('/')
                       and not os.path.basename(f).startswith('._')
                       and os.path.basename(f) != '.DS_Store']
        
        file_hashes = {}
        unique_files = []
        duplicate_files = []
        file_contents = {}  # Store file contents for display
        
        for file in valid_files:
            file_name = os.path.basename(file)
            extracted_path = os.path.join(output_folder, file_name)
            with zip_ref.open(file) as f:
                file_content = f.read()
                file_hash = hashlib.md5(file_content).hexdigest()
                if file_hash not in file_hashes:
                    file_hashes[file_hash] = file_name
                    unique_files.append(file_name)
                    with open(extracted_path, 'wb') as unique_file:
                        unique_file.write(file_content)
                    # Store file content for display
                    if file_name.lower().endswith(('.txt', '.csv', '.json', '.xml', '.html', '.log')):
                        try:
                            file_contents[file_name] = file_content.decode('utf-8')
                        except UnicodeDecodeError:
                            file_contents[file_name] = "Binary file (cannot display content)"
                    elif file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        # Save image to static folder
                        static_image_path = os.path.join(STATIC_FOLDER, file_name)
                        with open(static_image_path, 'wb') as img_file:
                            img_file.write(file_content)
                        file_contents[file_name] = url_for('static', filename=file_name)
                    else:
                        file_contents[file_name] = "Binary file (cannot display content)"
                else:
                    duplicate_files.append((file_name, file_hashes[file_hash]))
                    # Store file content for display
                    if file_name.lower().endswith(('.txt', '.csv', '.json', '.xml', '.html', '.log')):
                        try:
                            file_contents[file_name] = file_content.decode('utf-8')
                        except UnicodeDecodeError:
                            file_contents[file_name] = "Binary file (cannot display content)"
                    elif file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        # Save image to static folder
                        static_image_path = os.path.join(STATIC_FOLDER, file_name)
                        with open(static_image_path, 'wb') as img_file:
                            img_file.write(file_content)
                        file_contents[file_name] = url_for('static', filename=file_name)
                    else:
                        file_contents[file_name] = "Binary file (cannot display content)"
        
        return unique_files, duplicate_files, file_contents

def create_zip_from_folder(folder_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded."
        file = request.files['file']
        if file.filename == '':
            return "No selected file."
        
        zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(zip_path)
        files_list = list_main_zip_contents(zip_path)
        return render_template('index.html', files=files_list, filename=file.filename)
    return render_template('index.html', files=None)

@app.route('/extract/<filename>')
def extract(filename):
    zip_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Create a unique folder for this extraction
    unique_folder_name = str(uuid.uuid4())  # Generate a unique folder name
    extract_folder = os.path.join(EXTRACT_FOLDER, unique_folder_name)
    os.makedirs(extract_folder, exist_ok=True)
    
    # Extract unique files, identify duplicates, and store file contents
    unique_files, duplicate_files, file_contents = extract_unique_files(zip_path, extract_folder)
    
    # Create a ZIP file of the extracted unique files
    output_zip_path = os.path.join(OUTPUT_ZIP_FOLDER, f"{filename}unique_files{unique_folder_name}.zip")
    create_zip_from_folder(extract_folder, output_zip_path)
    
    return render_template('extracted.html', 
                           files=unique_files, 
                           filename=filename, 
                           zip_filename=f"{filename}unique_files{unique_folder_name}.zip", 
                           duplicates=duplicate_files, 
                           file_contents=file_contents)

@app.route('/download/<zip_filename>')
def download_zip(zip_filename):
    return send_from_directory(OUTPUT_ZIP_FOLDER, zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)