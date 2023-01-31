#1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#2
a = int(input())
h = int(input())
print((a*h)/2)

#3
n = int(input())
k = int(input())
print(k//n)
print(k%n)

#4
n = int(input())
print((n//60)%24,'',n%60)

#5
name = input()
print("Hello,", name + '!')

#6
n = int(input())
print("The next number for the number",n,"is",n+1)
print("The previous number for the number",n,"is",n-1)

#7
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

#8
a = int(input())

b = int(input())

l = int(input())

N = int(input())

print(((2*a*N - a)+2*l+2*b*(N-1)))