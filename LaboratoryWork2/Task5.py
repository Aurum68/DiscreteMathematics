n = 5
m = 8

def poit1(n: int, m:int) -> int:
    a=[[1] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] = a[i - 1][j] + a[i][j - 1]

    return a[n][m]


def poit2(n: int, m:int) -> int:
    a = [[[1, 0] for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= j or i == j + 1:
                if a[i-1][j][1] == 0:
                    a[i][j][0] = a[i - 1][j][0] + a[i][j - 1][0]
                    a[i][j][1] = 1
                else:
                    if a[i][j-1][1] == 0:
                        a[i][j][0] = a[i - 1][j - 1][0]
                    else:
                        a[i][j][0] = a[i - 1][j - 1][0] + a[i][j - 1][0]
                    a[i][j][1] = 1
            else:
                a[i][j][0] = a[i][j - 1][0]

    return a[n][m][0]


print("различных кратчайших путей ", poit1(n, m))
print("различных кратчайших путей с ограничением ", poit2(m, m))

if __name__ == '__main__':
    pass