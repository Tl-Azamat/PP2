num = [4,9,7]
def histogram(num):
    for i in num:
        for j in range(0 , i):
            print('*', end = "")
        print()
histogram(num)
