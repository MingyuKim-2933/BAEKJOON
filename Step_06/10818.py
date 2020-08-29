import sys

a = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

#Bubble Sort
for i in range(1,a+1):
    tmp = i - 1
    while tmp > 0 and num[tmp-1] > num[tmp]:
        num[tmp], num[tmp-1] = num[tmp-1], num[tmp]
        tmp -= 1
print(num[0],num[a-1])