num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
temp1 = 0
temp2 = 0

if num1 <= num2:
    temp1 = num1
    if temp1 >= num3:
        temp1 = num3

else:
    temp1 = num2
    if temp1 >= num3:
        temp1 = num3

if num4 >= num5:
    temp2 = num5

else:
    temp2 = num4

print(temp1+temp2-50)