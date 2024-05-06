def p(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1

x=int(input())
for i in range(2,x+1):
    if (x%i==0) and p(i)==1:
        print(i)
