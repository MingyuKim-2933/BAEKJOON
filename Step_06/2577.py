A=int(input())
B=int(input())
C=int(input())
multi = str(A * B * C)

for j in range(10):
    print(multi.count(str(j)))

# result = []
# for i in range(10):
#     result.append(0)
#
# for j in range(10):
#     for k in range(len(multi)):
#         if multi[k] == str(j):
#             result[j] += 1
#
# for l in range(10):
#     print(result[l])


