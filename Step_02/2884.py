num = input().split()

h = int(num[0])
m = int(num[1])

if h == 0 and m < 45:
    print(23, m+15)

elif m < 45:
    print(h-1, m+15)

else:
    print(h, m-45)