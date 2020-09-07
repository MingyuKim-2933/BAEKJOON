def d(a):
    if 0 <= a < 10:
        n = a + a

    elif 10 <= a <100:
        n = a + a // 10 + a % 10

    elif 100 <= a <1000:
        n = a + a // 100 + a // 10 % 10 + a % 10

    elif 1000 <= a <10000:
        n = a + a // 1000 + a // 100 % 10 + a // 10 % 10 + a % 10

    else:
        n = 10001

    return n


index = []
for i in range(10001):
    index.append(0)

for j in range(10001):
    if d(j) <= 10000:
        index[d(j)] = 1

for k in range(10001):
    if index[k] == 0:
        print(k)
