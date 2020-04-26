import random
import matplotlib.pyplot as plt
import math
import statistics

import numpy as np


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


# r(n) = r1(n) – mean(r1)
def centr_array(r1=[], n=0, mean=0):
    rn = (r1[n] - mean)
    return rn


def useful_component(n=0, m1=0, m2=0):
    vn = math.sin(((2 * math.pi) / m1) * n) + math.cos(((2 * math.pi) / m2) * n)
    return vn


def result(n=0, m1=0, m2=0, min=0, max=0):
    r1, mean = randome_date(n, min, float(max))
    xn = []
    fn = []
    for number in range(len(r1)):
        fn.append(useful_component(number, m1, m2))
        xn.append(fn[number] + centr_array(r1, number, mean))
    plt.plot(r1, "r--")  # Добавить данные на фигуру
    plt.plot(xn)
    plt.show()
    return fn, xn


def rollingsmooth(cx, l,en):
    cy = []
    asum = []
    xn = en.copy()
    for num in range(len(cx) - l // 2):
        for yn in range(l // 2, (-1 * l // 2) - 1, -1):
            asum.append(cx[num - yn])
        cy.append(sum(asum) / l + 1)
        print('summ',cy[num])
        asum.clear()

    for n in range(4):
        en = subs4(en)

    yn = subsvXN_EN(xn=xn,en=en)

    a = plt.plot(cx, label='Тестовая дискретная последовательность x(n)')  # Добавить данные на фигуру
    a = plt.plot(cy, 'g--', label='Результат скользящего сглаживания y(n)')
    a = plt.plot(yn, 'r--', label='Результат сглаживания четвертыми разностями y(n)')
    a = plt.legend()
    plt.show(a)
    return yn,cy


# Оценка качества сглаживания
def evaluation(fn, cy):
    j = float(0)
    print('fn', len(fn))
    print('cy', len(cy))
    for n in range(25,75,1):
        j = j + ((cy[n] - fn[n]) ** 2)
    return j

# сглаживанич 4тыми разностями
def subs4(xn):
    su = []
    for n in range(len(xn)-1):
        su.append(xn[n+1] - xn[n])
    return su


def subsvXN_EN(xn,en):
    yn = []
    for n in range(2,len(xn)-4):
        yn.append(xn[n]-en[n])
    return yn


#Экспоницальное сглаживание
def ecxp(a,xn):
    yn_exp = []
    temp = ((1.0-a)*1)+(a*xn[0])
    yn_exp.append(temp)
    for n in range(1,len(xn)):
        yn_exp.append(((1.0-a)*yn_exp[n-1])+(a*xn[n]))
    return yn_exp


def pered_feunct(xn,yn):
    hn = []
    print(len(cy))
    print(len(xn))
    for n in range(1,190,1):
        hn.append(yn[n]/xn[n])
    return hn


# r = f = 0....0.5
# m = L = 2,4,8
def smoothAHX(m):
    hf = []
    for i in np.arange(0.1, 0.6, 0.001):
        hf.append((math.sin(math.pi * i * m)) / (m * (math.sin(math.pi*i))))

    return hf
# -------RUN---------- #
n = 200
MIN = 0
MAX = 2.3
M1 = 47
M2 = 23



fn, xn = result(n=n, m1=M1, m2=M2, min=MIN, max=MAX)
xnn = xn.copy()
yn,cy = rollingsmooth(xn, 10,xn)




j = evaluation(fn, cy)
j1 = evaluation(fn, yn)

yn_exp = ecxp(float(-0.01),xn)
j2 = evaluation(fn, yn_exp)

hn = pered_feunct(xnn,yn_exp)
a = plt.plot(xnn, label='Тестовая дискретная последовательность x(n)')  # Добавить данные на фигуру

a = plt.plot(yn_exp, 'g--', label='Результат экспоненциального  сглаживания   y(n)')
a = plt.legend()
plt.show(a)



hf2 = smoothAHX(2)
hf4 = smoothAHX(4)
hf8 = smoothAHX(8)
hf16 = smoothAHX(16)
hf32 = smoothAHX(32)




b = plt.plot(hf2,'b', label='M2')
b = plt.plot(hf4, 'r', label='M4')
b = plt.plot(hf8, 'g', label='M8')
b = plt.plot(hf16, 'c', label='M16')
b = plt.plot(hf32, 'm', label='M32')

b = plt.legend()
plt.show(b)


print('eval', j)
print('eval1', j1)
print('eval2', j2)
