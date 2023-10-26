import matplotlib.pyplot as plt

n = 100
Price = [0] * (n + 1)
for i in range(1, n + 1):
    Price[i] += 5 + Price[i - 1]
C = [0] * (n + 1)
C[1] = Price[1]
for i in range(2, n + 1):
    C[i] = min(C[i - 1], C[i - 2]) + Price[i]
print(C)
plt.plot(C, color='k', linewidth=2)
plt.plot(C, "ro", color='#FFA500', markersize=4)
plt.title('Нахождение минимальной стоимости')
plt.xlabel('Номер ступеньки')
plt.ylabel('Минимальная стоимость')
plt.grid()
plt.show()