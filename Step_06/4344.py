import sys
N = int(sys.stdin.readline())
test=[]

for i in range(N):
    test.append(sys.stdin.readline().split())

for i in range(N):
    avg = 0
    count = 0
    for j in range(1,int(test[i][0])+1):
        avg += float    (test[i][j])/float(test[i][0])
    for j in range(1,int(test[i][0])+1):
        if float(test[i][j]) > avg+0.000000001:
            count += 1
    print('%.3f' % (count * 100 / float(test[i][0]))+'%')
