S = input()
a = []

for i in range(26):
    a.append(-1)
for i in range(26):
    temp = i+97
    for j in range(len(S)):
        if temp == ord(S[j]):
            a[i] = j
            break
    print(a[i], end=' ')

# for i in range(97,123): # find함수: 지정한 문자의 인덱스를 반환한다.
#     print(S.find(chr(i)), end=' ')
