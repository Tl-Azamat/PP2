a = int(input())
b = int(input())
c = int(input())

if a % 2 == 0:
    a = a
else:
    a = a + 1

if b % 2 == 0:
    b = b
else:
    b += 1

if c % 2 == 0:
    c = c
else:
    c = c + 1

print((a + b + c) // 2)