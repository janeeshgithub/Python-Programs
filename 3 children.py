x=list(input().strip())
for i in range(len(x)-1):
    if x[i]=='(' and x[i+1]==')':
        print(x[i],x[i+1],sep="")
