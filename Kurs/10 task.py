
def countPaths(n):

    zB = 1


    zADC = 0

    # На каждом шаге zADC умножается на 2(2 состояния) и добавляется zB, поскольку zB -
    # это количество путей на шаге n - 1, которое состоит из оставшихся 2 состояний.
    for i in range(1, n + 1):

        nzB = zADC * 3

        nzADC = (zADC * 2 + zB)


        zB = nzB
        zADC = nzADC


    return zB



n = 4
print(countPaths(n))

