import re

numberPattern = re.compile(r"\d{3}.\d{3}.\d{4}")
with open('data.txt', 'r') as file:
    contents = file.read()

    numberMatches = numberPattern.findall(contents)

    for number in numberMatches:
        print(number)
