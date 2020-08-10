import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    print("Case #"+str(i+1)+":",a+b)