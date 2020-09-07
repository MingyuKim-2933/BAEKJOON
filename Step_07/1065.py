def hansu(n):
    count = 0
    for i in range(1, int(n)+1):
        if i < 100:
            count += 1
        else:
            i = str(i)
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                count += 1
    return count


print(hansu(input()))
