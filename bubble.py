m = [3, 2, 1, 7, 6]


for i in range(len(m) - 1):
    for j in range(i, len(m)):
        if m[i] > m[j]:
            m[i], m[j] = m[j], m[i]
print(m)