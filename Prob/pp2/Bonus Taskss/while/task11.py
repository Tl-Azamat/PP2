a = int(input())
c = 0
while a != 0:
    b = int(input())
    if b != 0 and a < b:
        c += 1
    a = b
print(c)