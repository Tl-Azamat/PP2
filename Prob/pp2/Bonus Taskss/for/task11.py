a = int(input())
sum1 = 0
sum2 = 0
for i in range(1, a):
    x = int(input())
    sum1 += x

for i in range(1, a + 1):
    sum2 += i

sum = sum2 - sum1
print(sum)



  