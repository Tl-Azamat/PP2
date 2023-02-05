a = input()
b = ""
for i in range(0, len(a)):
    if(i % 3 != 0):
        b += a[i]
print(b)