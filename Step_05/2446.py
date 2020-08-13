a = int(input())
num = a * 2
j = 0

for i in range(1, num):
    if i <= a:
        print(' '*(i-1), end='')
    else:
        print(' '*(num-j), end='')
    print('*'*abs(num-i-j))
    j += 1
    if i == a:
        j += 2