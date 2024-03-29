import math
import matplotlib.pyplot as plt
import numpy as np


def plot():
    plt.scatter(data[0], data[1], label="Эксп")
    plt.plot(data[0], MSQ_arr, label="Лин")
    plt.plot(data[0], STEP_arr, label="Степ")
    plt.plot(data[0], POK_arr, label="Показ")
    plt.plot(data[0], KVADR_arr, label="Квадр")
    plt.grid()
    plt.legend()
    plt.show()


def best():
    msq, step, pok, kvadr = 0, 0, 0, 0
    for i in range(0, len(data[0])):
        msq += round((data[1][i] - MSQ_arr[i]) * (data[1][i] - MSQ_arr[i]), 2)
        step += round((data[1][i] - STEP_arr[i]) * (data[1][i] - STEP_arr[i]), 2)
        pok += round((data[1][i] - POK_arr[i]) * (data[1][i] - POK_arr[i]), 2)
        kvadr += round((data[1][i] - KVADR_arr[i]) * (data[1][i] - KVADR_arr[i]), 2)

    d = {'Линейная': msq, 'Степенная': step, 'Показательная': pok, 'Квадратичная': kvadr}
    razdel()
    print("Линейная", msq)
    print("Степ", step)
    print("Показ", pok)
    print("Квадр", kvadr)
    print("Наилучшая функция в данном случае - ", min(d, key=d.get))


def razdel():
    print("######################################################")


data = []
with open("var.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
print(data)
razdel()


def MSQ(arrX, arrY):
    sumX, sumY, sumX2, sumXY, n = 0, 0, 0, 0, len(arrX)
    for i in range(0, len(arrX)):
        sumX += arrX[i]
        sumY += arrY[i]
        sumX2 += arrX[i] * arrX[i]
        sumXY += arrX[i] * arrY[i]

    razdel()
    print("МНК")

    arr1 = [sumX2, sumX]
    arr2 = [sumX, n]
    arr3 = [sumXY, sumY]

    mainDet = np.linalg.det(np.array([arr1, arr2]))
    det1 = np.linalg.det(np.array([arr3, arr2]))
    det2 = np.linalg.det(np.array([arr1, arr3]))

    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    print("a =", a)
    print("b =", b)

    MSQ_Array_Y = []
    for i in range(0, n):
        newY = a * arrX[i] + b
        MSQ_Array_Y.append(round(newY, 2))

    razdel()

    return MSQ_Array_Y


def STEP(arrX, arrY):
    sumX, sumY, sumX2, sumXY, n = 0, 0, 0, 0, len(arrX)
    for i in range(0, len(arrX)):
        sumX += math.log(arrX[i])
        sumY += math.log(arrY[i])
        sumX2 += math.log(arrX[i]) * math.log(arrX[i])
        sumXY += math.log(arrX[i]) * math.log(arrY[i])

    razdel()
    print("СТЕП")

    arr1 = [sumX2, sumX]
    arr2 = [sumX, n]
    arr3 = [sumXY, sumY]

    mainDet = np.linalg.det(np.array([arr1, arr2]))
    det1 = np.linalg.det(np.array([arr3, arr2]))
    det2 = np.linalg.det(np.array([arr1, arr3]))

    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    print("a=", a)

    beta = round(math.e ** b, 2)
    print("b=", beta)

    STEP_Array_Y = []
    for i in range(0, n):
        newY = beta * (arrX[i] ** a)
        STEP_Array_Y.append(round(newY, 2))

    razdel()
    return STEP_Array_Y


def POK(arrX, arrY):
    sumX, sumY, sumX2, sumXY, n = 0, 0, 0, 0, len(arrX)
    for i in range(0, len(arrX)):
        sumX += arrX[i]
        sumY += math.log(arrY[i])
        sumX2 += arrX[i] * arrX[i]
        sumXY += arrX[i] * math.log(arrY[i])

    razdel()
    print("ПОК")

    arr1 = [sumX2, sumX]
    arr2 = [sumX, n]
    arr3 = [sumXY, sumY]

    mainDet = np.linalg.det(np.array([arr1, arr2]))
    det1 = np.linalg.det(np.array([arr3, arr2]))
    det2 = np.linalg.det(np.array([arr1, arr3]))

    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    print("a=", a)

    beta = round(math.e ** b, 2)
    print("b=", beta)

    POK_Array_Y = []
    for i in range(0, n):
        newY = beta * (math.e ** (a * arrX[i]))
        POK_Array_Y.append(round(newY, 2))

    razdel()
    return POK_Array_Y


def KVADR(arrX, arrY):
    sumX, sumX2, sumX3, sumX4, sumX2Y, sumXY, sumY, n = 0, 0, 0, 0, 0, 0, 0, len(arrX)
    for i in range(0, len(arrX)):
        sumX4 += pow(arrX[i], 4)
        sumX3 += pow(arrX[i], 3)
        sumX2 += pow(arrX[i], 2)
        sumX += pow(arrX[i], 1)
        sumX2Y += pow(arrX[i], 2) * arrY[i]
        sumXY += arrX[i] * arrY[i]
        sumY += arrY[i]

    razdel()
    print("КВАДР")

    arr1 = [sumX4, sumX3, sumX2]
    arr2 = [sumX3, sumX2, sumX]
    arr3 = [sumX2, sumX, n]
    arr4 = [sumX2Y, sumXY, sumY]

    mainDet = np.linalg.det(np.array([arr1, arr2, arr3]))
    det1 = np.linalg.det(np.array([arr4, arr2, arr3]))
    det2 = np.linalg.det(np.array([arr1, arr4, arr3]))
    det3 = np.linalg.det(np.array([arr1, arr2, arr4]))

    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    c = round((det3 / mainDet), 2)
    print("a=", a)
    print("b=", b)
    print("c=", c)

    KVADR = []
    for i in range(0, n):
        newY = a * pow(arrX[i], 2) + b * arrX[i] + c
        KVADR.append(round(newY, 2))

    razdel()
    return KVADR


MSQ_arr = MSQ(data[0], data[1])
STEP_arr = STEP(data[0], data[1])
POK_arr = POK(data[0], data[1])
KVADR_arr = KVADR(data[0], data[1])
best()
plot()
