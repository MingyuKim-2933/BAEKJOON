num1 = int(input())
num2 = int(input())

num2_1 = num2%10
num2_10 = num2%100-num2_1
num2_100 = num2%1000-num2_10-num2_1

print(num1*num2_1)
print(int(num1*num2_10/10))
print(int(num1*num2_100/100))
print(num1*num2)