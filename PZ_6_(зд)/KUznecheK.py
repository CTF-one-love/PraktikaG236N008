"""def h(n):
    b = [None] + ([0] * max(3, n))
    b[1] = 1
    b[2] = 1
    for i in range(3, n + 1):
        b[i] = b[i - 1] + b[i - 2]
        if i % 3 == 0:
            b[i] += b[i // 3]
    return b[n]

print('Количество способов достичь её:', h(int(input('Введите конечную точку: '))))"""


def count_ways_to_n(n):
    if n < 1:
        return 0, 0
    # Создаем массив для хранения количества способов достичь каждой позиции
    ways = [0] * (n + 1)
    cost = [0] * (n + 1)

    # Начальная позиция (1) всегда имеет один способ достижения - сам собой.
    ways[1] = 1
    cost[1] = 0
    for i in range(2, n + 1):
        # Рассматриваем все возможные прыжки (+1, +3, *3)
        if i - 1 >= 1:
            ways[i] += ways[i - 1]
            cost[i] += cost[i - 1] + 2
        if i - 3 >= 1:
            ways[i] += ways[i - 3]
            cost[i] += cost[i - 3] + 6
        if i % 3 == 0 and i // 3 >= 1:
            ways[i] += ways[i // 3]
            ways[i] += ways[i // 3] + 15

    return ways[n], cost[n]
n = 100
ways, total_cost = count_ways_to_n(n)
print(ways, "  ", total_cost)