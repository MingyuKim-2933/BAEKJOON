d = input().split()
a = int(d[0])
b = int(d[1])
c = int(d[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)