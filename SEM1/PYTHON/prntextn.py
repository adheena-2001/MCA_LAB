filename=raw_input('enter a filename:')
if'.'in filename:
    name,extension=filename.split('.')
    print('the extension of the file is:' +extension)
else:
    print('Invalid filename format.Please include the file extension(eg:filename.txt)')
