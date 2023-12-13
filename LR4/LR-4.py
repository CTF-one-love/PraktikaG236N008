import matplotlib.pyplot as plt
import random
import pandas as pd

def my_rand1(n: int) -> list:
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data

b1 = my_rand1(10)
print(b1)

def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

d1 = count_rate(b1)
print(d1)

def sort_rate(counted_rate: dict):
    """    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

f1 = sort_rate(d1)
print(f1)

def crate_dataframe(sorted_date: dict):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df

df = crate_dataframe(f1)
print(df)

def probability_solving(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

print(probability_solving(df))

a = probability_solving(crate_dataframe(sort_rate(count_rate(my_rand1(10)))))

a['Вероятность'].plot(kind='bar', legend=True)
plt.show()

