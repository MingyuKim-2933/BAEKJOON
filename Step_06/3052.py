x = []
count = 10
over = 0
for i in range(10):
    x.append(int(input()) % 42)

for j in range(10):
    for k in range(j+1, 10):
        if x[j] == x[k]:
            over = 1
    if over == 1:
        count -= 1
        over = 0
print(count)
