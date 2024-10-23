import streamlit as st
import pandas as pd
import pickle
from fpdf import FPDF
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import io

# Load the saved model and label encoders
with open('liver_cirrhosis_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('label_encoders.pkl', 'rb') as encoders_file:
    label_encoders = pickle.load(encoders_file)

# List of categorical columns that need encoding
categorical_cols = ['Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Status', 'Drug']

# List of all features in the model, in the correct order
feature_columns = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema',
                   'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 
                   'Platelets', 'Prothrombin']

# Set custom CSS for background images and styling
st.markdown(""" 
    <style>
    .main-title {
        font-size: 48px;
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        padding-top: 20px;
        margin-bottom: 10px;
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
    }
    .sub-header {
        font-size: 28px;
        color: #ff6347;
        margin-top: 40px;
        text-align: center;
    }
    .input-area {
        font-size: 16px;
        margin-bottom: 20px;
    }
    .btn-style {
        background-color: #4B9CD3;
        color: white;
        font-size: 18px;
        padding: 10px;
        margin-top: 30px;
    }
    .form-container {
        background: rgba(255, 255, 255, 0.8);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    }
    .prediction-result {
        font-size: 24px;
        padding: 20px;
        color: white;
        background: rgba(0, 128, 0, 0.7);
        text-align: center;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# App title with enhanced style
st.markdown('<h1 class="main-title">Liver Cirrhosis Stage Prediction</h1>', unsafe_allow_html=True)

# Create a form container with background transparency
with st.container():
    # Input form for user data with improved layout
    st.markdown('<h2 class="sub-header">Enter Patient Details</h2>', unsafe_allow_html=True)

    # Collect user inputs for all the features
    col1, col2 = st.columns(2)
    with col1:
        Patient_Name = st.text_input('Patient Name')
        Patient_ID = st.text_input('Patient ID')
        N_Days = st.number_input('Number of Days (N_Days)', min_value=0, max_value=5000, step=1)
        Age = st.number_input('Age (in days)', min_value=0, max_value=30000, step=1)
        Sex = st.selectbox('Sex', options=['', 'M', 'F'])
        Ascites = st.selectbox('Ascites', options=['', 'Y', 'N'])
        Hepatomegaly = st.selectbox('Hepatomegaly', options=['', 'Y', 'N'])
        Spiders = st.selectbox('Spiders', options=['', 'Y', 'N'])

    with col2:
        Edema = st.selectbox('Edema', options=['', 'Y', 'N'])
        Bilirubin = st.number_input('Bilirubin', min_value=0.0, max_value=50.0, step=0.1)
        Cholesterol = st.number_input('Cholesterol', min_value=0.0, max_value=500.0, step=0.1)
        Albumin = st.number_input('Albumin', min_value=0.0, max_value=10.0, step=0.1)
        Copper = st.number_input('Copper', min_value=0.0, max_value=500.0, step=1.0)
        Alk_Phos = st.number_input('Alk_Phos', min_value=0.0, max_value=2000.0, step=1.0)

    SGOT = st.number_input('SGOT', min_value=0.0, max_value=1000.0, step=1.0)
    Tryglicerides = st.number_input('Tryglicerides', min_value=0.0, max_value=500.0, step=1.0)
    Platelets = st.number_input('Platelets', min_value=0.0, max_value=1000.0, step=1.0)
    Prothrombin = st.number_input('Prothrombin', min_value=0.0, max_value=20.0, step=0.1)
    Status = st.selectbox('Status', options=['', 'C', 'D','CL'])
    Drug = st.selectbox('Drug', options=['', 'placebo', 'D-penicillamine'])
    
    Email = st.text_input('Email Address')

# Check if any required field is not filled
if st.button('Predict Stage and Send Email', key='predict-btn'):
    if '' in [Sex, Ascites, Hepatomegaly, Spiders, Edema, Status, Drug, Email, Patient_Name, Patient_ID]:
        st.error("Please fill in all the required fields.")
    else:
        # Create a dictionary for the inputs
        input_data = {
            'N_Days': N_Days,
            'Age': Age,
            'Sex': Sex,
            'Ascites': Ascites,
            'Hepatomegaly': Hepatomegaly,
            'Spiders': Spiders,
            'Edema': Edema,
            'Bilirubin': Bilirubin,
            'Cholesterol': Cholesterol,
            'Albumin': Albumin,
            'Copper': Copper,
            'Alk_Phos': Alk_Phos,
            'SGOT': SGOT,
            'Tryglicerides': Tryglicerides,
            'Platelets': Platelets,
            'Prothrombin': Prothrombin,
            'Status': Status,
            'Drug': Drug
        }

        # Convert the input data into a DataFrame
        input_df = pd.DataFrame([input_data])

        # Ensure column order matches the training set
        input_df = input_df[feature_columns]

        # Apply the same label encoders to the new data and handle unseen labels
        for col in categorical_cols:
            if col in label_encoders:
                input_df[col] = input_df[col].apply(lambda x: label_encoders[col].transform([x])[0]
                                                    if x in label_encoders[col].classes_ else -1)  # Handle unseen labels with -1

        # Make predictions on the new patient data
        prediction = loaded_model.predict(input_df)[0]

        # Prepare the prediction message
        stage_message = f"Stage {prediction}"
        color = {1: 'green', 2: 'yellow', 3: 'red'}.get(prediction, 'purple')

        # Display the prediction result with improved styling
        st.markdown(f'<div class="prediction-result" style="background-color:{color};">{stage_message}</div>', unsafe_allow_html=True)

        # Create a PDF using FPDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Add title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Liver Cirrhosis Stage Prediction Report", ln=True, align="C")

        # Add patient details with bold headings
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Patient Details:", ln=True)

        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Patient Name: {Patient_Name}", ln=True)
        pdf.cell(0, 10, f"Patient ID: {Patient_ID}", ln=True)
        pdf.cell(0, 10, f"Number of Days: {N_Days}", ln=True)
        pdf.cell(0, 10, f"Age: {Age}", ln=True)
        pdf.cell(0, 10, f"Sex: {Sex}", ln=True)
        pdf.cell(0, 10, f"Ascites: {Ascites}", ln=True)
        pdf.cell(0, 10, f"Hepatomegaly: {Hepatomegaly}", ln=True)
        pdf.cell(0, 10, f"Spiders: {Spiders}", ln=True)
        pdf.cell(0, 10, f"Edema: {Edema}", ln=True)
        pdf.cell(0, 10, f"Bilirubin: {Bilirubin}", ln=True)
        pdf.cell(0, 10, f"Cholesterol: {Cholesterol}", ln=True)
        pdf.cell(0, 10, f"Albumin: {Albumin}", ln=True)
        pdf.cell(0, 10, f"Copper: {Copper}", ln=True)
        pdf.cell(0, 10, f"Alk_Phos: {Alk_Phos}", ln=True)
        pdf.cell(0, 10, f"SGOT: {SGOT}", ln=True)
        pdf.cell(0, 10, f"Tryglicerides: {Tryglicerides}", ln=True)
        pdf.cell(0, 10, f"Platelets: {Platelets}", ln=True)
        pdf.cell(0, 10, f"Prothrombin: {Prothrombin}", ln=True)
        pdf.cell(0, 10, f"Status: {Status}", ln=True)
        pdf.cell(0, 10, f"Drug: {Drug}", ln=True)
        pdf.cell(0, 10, f"Predicted Stage: {stage_message}", ln=True)

        # Save the PDF to a string
        pdf_output = pdf.output(dest='S').encode('latin1')

        # Create a BytesIO object from the PDF string
        pdf_output_io = io.BytesIO(pdf_output)

        # Create a download link for the PDF report
        st.download_button(
            label="Download PDF Report",
            data=pdf_output_io,
            file_name="liver_cirrhosis_report.pdf",
            mime="application/pdf"
        )

        # Function to send the email with the PDF attached
        def send_email(to_email, subject, body, attachment):
            try:
                # Set up the SMTP server
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                smtp_user = 'adheena282001@gmail.com'  # Replace with your email
                smtp_password = 'bwna crdl duho lfkq'  # Replace with your app password

                # Create the email
                msg = MIMEMultipart()
                msg['From'] = smtp_user
                msg['To'] = to_email
                msg['Subject'] = subject

                # Attach the body with the msg instance
                msg.attach(MIMEText(body, 'plain'))

                # Attach the PDF file
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(pdf_output_io.getvalue())  # Read PDF data from BytesIO
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="liver_cirrhosis_report.pdf"')
                msg.attach(part)

                # Send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()  # Upgrade the connection to secure
                    server.login(smtp_user, smtp_password)
                    server.send_message(msg)

                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")

        # Send the email
        email_subject = "Liver Cirrhosis Stage Prediction Report"
        email_body = "Attached is your Liver Cirrhosis Stage Prediction Report."
        send_email(Email, email_subject, email_body, pdf_output_io)
