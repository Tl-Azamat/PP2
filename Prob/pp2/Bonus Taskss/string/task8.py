a = input()
x = a[:a.find('h')]
y = a[a.find('h'): a.rfind('h') + 1]
z = a[a.rfind('h') + 1:]
print(x + y[::-1] + z)