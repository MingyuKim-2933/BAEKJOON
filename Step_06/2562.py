x=[]
max=0
for i in range(9):
    x.append(int(input()))
    if x[i]>=max:
        max = x[i]
        count = i+1
print(max)
print(count)
# print((x.index(max))+1) ##list에서 index 사용