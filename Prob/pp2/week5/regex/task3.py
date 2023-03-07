import re
file = open("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week5/regex/text.txt", "r", encoding = "UTF8")


result = re.findall('[a-z]+_', file.read())
print(result)