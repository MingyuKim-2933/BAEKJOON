a= int(input())
num = a*a*2+1
change= 1

for i in range(1, num):
    if a % 2 == 0 and change == -1:
        if i % 2 ==1: print(' ', end='')
        elif i % 2 ==0: print('*', end='')
    else:
        if i % 2 == 1: print('*', end='')
        elif i % 2 == 0: print(' ', end='')
    if i % a == 0 and i != num-1:
        print()
        change = change * -1