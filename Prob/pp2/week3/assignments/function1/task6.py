def rev_function(text):
    x=text
    index=-1
    reverse=[]
    i=0
    while i < len(x):
        reverse.append(x[index])
        index=index-1
        i+=1
    final=' '.join(reverse)
    print(final)

text = input().split()
rev_function(text)

#2
def reversed():
    s = input().split()
    print(*s[::-1])
reversed()
