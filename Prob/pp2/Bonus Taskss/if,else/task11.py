a = int(input())
b = int(input())
c = int(input())
d = int(input())
dx = abs(a - c)
dy = abs(b - d)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')