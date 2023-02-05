a = int(input())
i = 1
s = 0
while 2 ** i <= a:
    s = 2**i
    i+=1

print(i - 1, s)


