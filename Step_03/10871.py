n, x = input().split()
a = input().split()

for i in range(int(n)):
    if int(x) > int(a[i]):
        print(int(a[i]),"",end='')