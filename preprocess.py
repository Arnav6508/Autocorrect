import re

def preprocess(file_name):
    with open(file_name) as file:
        data = file.read()
    
    data = data.lower()
    words = re.findall('\w+', data)

    return words