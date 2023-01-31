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