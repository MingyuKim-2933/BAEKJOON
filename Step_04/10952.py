import sys
while(1):
    a, b = sys.stdin.readline().split()
    if(a=='0') and (b=='0'):
        break
    print(int(a)+int(b))

