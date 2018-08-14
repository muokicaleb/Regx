import re

numerPattern = re.compile(r"\d(3).\d(3).\d(4)")
with open('data.txt', 'r') as file:
    contents = file.read()

    numberMatches = numerPattern.finditer(contents)

    for number in numberMatches:
        print(number)
