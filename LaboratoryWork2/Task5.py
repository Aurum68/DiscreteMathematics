def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinations(n, k):
    if n >= k:
        return factorial(n) // (factorial(k) * factorial(n - k))
    else:
        return 0

def punkt1(widght, height):
    return combinations(widght + height, height)

def punkt2(widght, height):
    return combinations(widght+1, height)


widght = height = 18
print("Всего кратчайших путей ", punkt1(widght, height))
print("Кратчайших путей с ограничением ", punkt2(widght, height))