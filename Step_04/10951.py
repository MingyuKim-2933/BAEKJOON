import sys
n=0
while(1):
    try:
        a, b = sys.stdin.readline().split()
        print(int(a)+int(b))
    except:
        break