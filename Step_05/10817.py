num = list(map(int, input().split()))
def swap(i,j):
    num[i], num[j] = num[j], num[i]

#Bubble Sort
# for i in range (len(num)):
#     for j in range (len(num)-1):
#         if(num[j] > num[j+1]):
#             swap(j, j+1)
#
# print(num[1])

#Selection Sort
# for i in range (len(num)):
#     min = i
#     for j in range (i+1, len(num)):
#         if(num[min] >= num[j]): min = j
#     swap(i, min)
#
# print(num[1])

#Insertion Sort
# for i in range(1, len(num)):
#     tmp = num[i]
#     j = i-1
#     while(j >= 0 and tmp < num[j]):
#         num[j+1] = num[j]
#         j -= 1
#     num[j+1] = tmp
#
# print(num[1])

#Insertion Sort2
for i in range(1, len(num)):
    tmp = i
    while tmp > 0 and num[tmp-1] > num[tmp]:
        swap(tmp - 1, tmp)
        tmp -= 1

print(num[1])