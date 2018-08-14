import re

emailPattern = re.compile(r"[a-zA-Z]+@[a-zA-Z]+\.(com|net|org|edu)")
with open('data.txt', 'r') as file:
    contents = file.read()

    emailMatches = emailPattern.finditer(contents)

    for email in emailMatches:
        print(email)
