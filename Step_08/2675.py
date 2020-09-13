T = int(input())
S = []
N = []
temp = 0
count = 0

for i in range(T):
    A, B = map(str, input().split())
    N.append(len(B) * int(A))
    for j in range(len(B)):
        for k in range(int(A)):
            S.append(B[j])
for i in range(len(S)):
    print(S[i], end='')
    temp += 1
    if temp == N[count]:
        print()
        temp = 0
        count += 1
