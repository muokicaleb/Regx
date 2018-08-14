import re

emailPattern = re.compile(r"[a-zA-Z0-9.+-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
with open('data.txt', 'r') as file:
    contents = file.read()

    emailMatches = emailPattern.finditer(contents)

    for email in emailMatches:
        print(email)
