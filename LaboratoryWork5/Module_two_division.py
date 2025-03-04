def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))


def poly_divmod(A, B):
    """
    Деление многочленов A на B по модулю 2.
    A и B - списки коэффициентов многочленов (от старшего к младшему).
    Возвращает частное и остаток.
    """


    A_clean = A[A.index(1): ]
    B_clean = B[B.index(1): ]
    m, n = len(A_clean), len(B_clean)

    # Проверка деления на 0
    if n == 0:
        raise ValueError("Деление на ноль")
    if m < n:
        return [0], A  # Частное 0, остаток A

    # Подготовка частного
    Q = [0] * (m - n + 1)

    # Основной алгоритм деления
    while len(A_clean) >= len(B_clean):
        # Делаем шаг в частном
        Q[len(Q) - (len(A_clean) - len(B_clean)) - 1] = 1
        buf = [0 for _ in range(len(A_clean))]
        for i in range(len(B_clean)):
            buf[i] = 1 if B_clean[i] == Q[list_rindex(Q, 1)] else 0

        # Вычитаем B из A (по модулю 2)
        for i in range(len(buf)):
            A_clean[i] ^= buf[i]

        if 1 in A_clean:
            A_clean = A_clean[A_clean.index(1): ]
        else:
            A_clean = [0]
    return Q, A_clean