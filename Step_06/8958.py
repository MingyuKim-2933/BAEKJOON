import sys
test = list([])
a = int(sys.stdin.readline())
for i in range(a):
    test.append(sys.stdin.readline())

for i in range(a):
    count = 0
    sum = 0
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
