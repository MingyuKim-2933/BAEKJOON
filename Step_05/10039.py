n=[]
sum=0
for i in range(0,5):
    n.append(int(input()))
    if(n[i]<40):
        n[i]=40
    sum=sum+n[i]
    avg=sum/5
print(int(avg))