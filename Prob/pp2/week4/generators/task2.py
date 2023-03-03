a = int(input())
def EvenN(a):
    for i in range(0, a + 1):
        if i % 2 == 0:
            print(i)
        i += 1
EvenN(a)