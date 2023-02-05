a = input()
b = a[:a.find(" ")]
c = a[a.find(" ") + 1:]
print(c +  " " + b)