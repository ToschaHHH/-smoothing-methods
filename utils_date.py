import random


def randome_date(n=0, min_rnd=0, max_rnd=0):
    r1 = []  # Массив для хранения случайных чисел
    random.seed(44)
    for number in range(n):
        r1.append(random.uniform(min_rnd, max_rnd))  # Добавлям рандомные значения
        print(r1[number])
    MEAN = sum(r1) / n  # mean(r1) среднее значение случайных чисел
    print("MEAN = ", MEAN)
    # plt.plot(r1, "r.")  # Добавить данные на фигуру
    # plt.plot(r1)
    # plt.show()
    return r1, MEAN