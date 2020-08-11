n = int(input())
temp = n
count=1
if(n==0):
    print(1)
    exit()

while(1):
        a=int(temp/10)
        b=temp%10
        sum=a+b
        temp=(10*b)+(sum%10)
        if(temp==n and count!=1):
            print(count)
            break
        count+=1