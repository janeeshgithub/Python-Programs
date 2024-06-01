import time
x="kadambari"
t=''
i=0
k='abcdefghijklmnopqrstuvwxyz'
while(t!=x):
    m=0
    while(k[m]!=x[i]):
        print(t,k[m],sep="")
        time.sleep(0.1)
        m+=1
    t+=x[i]
    i+=1
    print(t)
    time.sleep(0.1)








