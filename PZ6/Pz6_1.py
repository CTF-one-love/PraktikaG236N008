def h(n):
    b = [None] + ([0] * max(3, n))
    b[1] = 1
    b[2] = 1
    for i in range(3, n + 1):
        b[i] = b[i - 1] + b[i - 2]
        if i % 3 == 0:
            b[i] += b[i // 3]
    return b[n]

print('Количество способов достичь её:', h(int(input('Введите конечную точку: '))))