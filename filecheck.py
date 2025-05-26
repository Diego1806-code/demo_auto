import os

def check_json():
    if os.path.exists('data.json'):
        os.remove('data.json')
        print("json has been deleted")
    else:
        print('data.json does not exist')

def check_pdf():
    if os.path.exists('output.pdf'):
        os.remove('output.pdf')
        print('output.pdf has been deleted')
    else:
        print('output.pdf does not exist')

