#1
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

#2
n = int(input())
if n>0 :
    print(1)
elif n==0 :
    print(0)
else:
    print(-1)

#3
a = int(input())
b = int(input())
x = int(input())
y = int(input())
cnt = 0
if (a+b)%2==0:
    cnt+=1
if (x+y)%2==0:
    cnt+=1
if cnt==2:
    print("Yes")
else :
    print("No")

#4
a = int(input())
if a % 4 == 0 and (a % 100 != 0 or a % 400 ==0):
    print("Yes")
else:
    print("No")

#5
a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))

#6
a = int(input())
b = int(input())
c = int(input())
if a==b==c :
    print(3)
elif a==b or b==c or a==c:
    print(2)
else :
    print(0)    

#7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d or a == d or b == c:
    print("Yes")
else:
    print("No")

#8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a-c)<=1 and abs(b-d)<=1:
    print("Yes")
else:
    print("No") 

#9
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d or a == d or b == c:
    print("No")
else:
    print("Yes")

#10
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d or abs(a-c)==abs(b-d):
    print("Yes")
else :
    print("No")    

#11
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

#12
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

#13
n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y

if x < y:
    print(x)
else:
    print(y)

