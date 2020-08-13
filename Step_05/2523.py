a = int(input())
num = a*2
for i in range(1, num):
    count=num-i
    if i <= a:
        print('*'*i)
    else:
        print('*' * count)