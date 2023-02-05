a = input()
x = a.find('f')
y = a.rfind('f')
if x == -1:
    print()
elif x == y:
    print(x)
else:
    print(x, y)
