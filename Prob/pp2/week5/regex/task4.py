import re
file = open("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week5/regex/text.txt", "r", encoding = "UTF8")


result = re.findall('[A-Z]+[a+z]+', file.read())
print(result)