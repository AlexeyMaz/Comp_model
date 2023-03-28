from matplotlib import pyplot as plt
import math
from random import uniform
from scipy import integrate

n = 13
N = 5000


def triangle_f1(x):
    return (10 * x) / n


def triangle_f2(x):
    return 10 * (x - 20) / (n - 20) + 20


def triangle_fn():
    print("Треугольник")
    arr_x = []
    for i in range(23):
        arr_x.append(i)

    arr_y1 = []
    arr_y2 = []
    for x in arr_x:
        y = round(triangle_f1(x), 2)
        arr_y1.append(y)
        y = round(triangle_f2(x), 2)
        arr_y2.append(y)

    arr_y3 = [arr_y1[0], arr_y2[0]]
    arr_x1 = [0, 0]
    fig, ax = plt.subplots()
    plt.grid()

    a = round(max(arr_y2), 0)
    b = max(arr_x)

    M = 0
    for i in range(N + 1):
        x = uniform(min(arr_x), max(arr_x))
        max_y = round(max(arr_y2), 0)
        min_x = min(arr_x)
        y = uniform(min_x, max_y)

        if y > round(triangle_f2(x), 2) or y < round(triangle_f1(x), 2):
            ax.plot(x, y, 'p', color='r')
        else:
            ax.plot(x, y, 'p', color='g')
            M += 1

    S = M / N * a * b
    area = round(a * b / 2, 5)
    S = round(S, 5)
    print(f"Кол-во точек, лежащих внутри фигуры = {M}\nТочная площадь = {area}\nПлощадь = {S}\n")
    ax.plot(arr_x, arr_y1, 'black')
    ax.plot(arr_x, arr_y2, color='black')
    ax.plot(arr_x1, arr_y3, color='black')

    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


def fun_int(x):
    return math.sqrt(29 - n * math.pow(math.cos(x), 2))


def integral_fn():
    print("Интеграл")
    x = []
    y = []

    i = 0
    while i != 7:
        x.append(i)
        y.append(round(fun_int(i), 2))
        i = round(i + 0.1, 1)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'black')
    plt.grid()

    M = 0
    a = round(max(x), 0)
    b = round(max(y), 2)

    for i in range(N + 1):
        x = uniform(0, a)
        y = uniform(0, b)

        if y < fun_int(x):
            ax.plot(x, y, 'p', color='g')
            M += 1
        else:
            ax.plot(x, y, 'p', color='r')

    f = lambda x: math.sqrt(29 - n * math.pow(math.cos(x), 2))
    s = integrate.quad(lambda x: math.sqrt(29 - n * math.pow(math.cos(x), 2)), 0, 7)

    S = round(M / N * a * b, 5)
    print(f"Кол-во точек, лежащих внутри фигуры = {M}\nТочное значение интеграла = {round(s[0], 5)}\n"
          f"Определенный интеграл = {S}\n")

    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


def circle_fn():
    print("Круг")
    x = []
    y = []

    i = 0
    while i <= 2 * n:
        x.append(n + n * math.cos(i))
        y.append(n + n * math.sin(i))
        i = round(i + 0.1, 1)

    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, 'black')

    M = 0
    for i in range(N + 1):
        x = uniform(0, 2 * n)
        y = uniform(0, 2 * n)
        if math.pow((x - n), 2) + math.pow((y - n), 2) < math.pow(n, 2):
            ax.plot(x, y, 'p', color='g')
            M += 1
        else:
            ax.plot(x, y, 'p', color='r')

    area = round(math.pi * n ** 2, 5)
    S = round(M / N * ((2 * n) ** 2), 5)
    pi = round(S / math.pow(n, 2), 5)
    print(f"Точная площадь круга = {area}\nКол-во точек, лежащих внутри фигуры = {M}\nПлощадь круга = {S}\n"
          f"Приближенное значение pi = {pi}\n")

    ax.axis('equal')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


def p_fn(f, a, b):
    return math.sqrt(a * math.pow(math.cos(f), 2) + b * math.pow(math.sin(f), 2))


def pp(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def ff(x, y):
    if x > 0:
        return math.atan(y / x)
    elif x < 0:
        return math.atan(y / x) + math.pi
    elif y > 0:
        return math.pi / 2
    else:
        return math.pi * (3 / 2)


def eleps_fn():
    print("Эллипс")
    A = n + 10
    B = n - 10
    x = []
    y = []

    i = 0
    while i <= 2 * math.pi + 1:
        x.append(p_fn(i, A, B) * math.cos(i))
        y.append(p_fn(i, A, B) * math.sin(i))
        i = round(i + 0.1, 1)

    a = max(x)
    b = max(y)
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, 'black')

    M = 0
    for i in range(N + 1):
        x = uniform(-a, a)
        y = uniform(-b, b)

        if pp(x, y) < p_fn(ff(x, y), A, B):
            ax.plot(x, y, 'p', color='g')
            M += 1
        else:
            ax.plot(x, y, 'p', color='r')

    S = round(M / N * a * b * 4, 5)
    ss = round(math.pi / 2 * (A + B), 5)

    f = lambda x: A * math.pow(math.cos(x), 2) + B * pow(math.sin(x), 2)
    s = integrate.quad(lambda x: A * math.pow(math.cos(x), 2) + B * pow(math.sin(x), 2), 0, math.pi / 2)

    print(f"Кол-во точек, лежащих внутри фигуры = {M}\nТочная площадь = {ss}\n"
          f"Точная площадь через интеграл = {round(2 * s[0], 5)}\nПлощадь = {S}")

    ax.axis('equal')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


def draw():
    print(f'Число точек: {N}\n')

    # triangle_fn()
    # integral_fn()
    # circle_fn()
    eleps_fn()


draw()
