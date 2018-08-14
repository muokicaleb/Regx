import re

numerPattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('data.txt', 'r') as file:
    contents = file.read()

    numberMatches = numerPattern.finditer(contents)

    for number in numberMatches:
        print(number)
