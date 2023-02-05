a = input()
x = a[:a.find('h') + 1]
y = a[a.find('h')+ 1  : a.rfind('h')]
z = a[a.rfind('h'):]
print(x + y.replace('h', 'H') + z)