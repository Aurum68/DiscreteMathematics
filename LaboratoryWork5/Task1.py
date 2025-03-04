import itertools
import  random
import Module_two_division

n = 15
m = 11
p = [1, 0, 0, 1, 1]

G = [[0 for i in range(n)] for j in range(m)]


def sum_mod_2(*codes: list[int]) -> list[int]:
    result = [0 for i in range(len(codes[0]))]
    for i in range(len(codes[0])):
        for j in range(len(codes)):
            result[i] = (result[i] + codes[j][i]) % 2
    return result


def code_distance(code1: list[int], code2: list[int]) -> int:
    distance = 0
    for i in range(len(code1)):
        distance += (code1[i] + code2[i]) % 2
    return distance


def polynomial_multiplication(polynomial1: list[int], polinomial2: list[int]) -> list[int]:
    result = [0 for i in range(len(polynomial1) + len(polinomial2))]
    for i in range(len(polynomial1)):
        for j in range(len(polinomial2)):
            result[i + j] ^= (polynomial1[i] * polinomial2[j])
    return result


for i in range(len(G)):
    count = 0
    for j in range(len(G[i]) - i - 5, len(G[i]) - i):
        G[i][j] = p[count]
        count += 1

print("Порождающая матрица:")
for g in G:
    print(g)

code_table = G.copy()
count = 2

indexes = [i for i in range(len(G))]
while count <= len(G):
    combs = list(itertools.combinations(indexes, count))
    for comb in combs:
        buffer = []
        for i in comb:
            buffer.append(G[i])
        code_table.append(sum_mod_2(*buffer))
    count += 1


print()

print("Фрагмент таблицы кодов")
for i in range(50):
    print(code_table[i])

min_distance = -1
for i in range(len(code_table) - 1):
    for j in range(i + 1, len(code_table)):
        if min_distance < 0:
            min_distance = code_distance(code_table[i], code_table[j])
        else:
            d = code_distance(code_table[i], code_table[j])
            min_distance = d if d < min_distance else min_distance
print("\nМинимальное кодовое расстояние = ", min_distance)

print("\nФрагмент таблицы кодовых расстояний")
for i in range(10):
    for j in range(i + 1, i + 5):
        print(f"d({code_table[i]}, {code_table[j]}) = {code_distance(code_table[i], code_table[j])}")

print(f"\nКратность гарантированно исправляемых кодом ошибок = {(min_distance - 1) // 2 if min_distance % 2 == 1 else min_distance // 2 - 1}")
print(f"Кратность гарантированно обнаруживаемых кодом ошибок = {min_distance - 1}")

print("\nДемонстрация делимости кода на производящий многочлен")

flag = True
for code in code_table:
    q, r = Module_two_division.poly_divmod(code, p)
    if r != [0]:
        flag = False
        break
print("Остаток от деления всех кодов на производящий многочлен = 0" if flag else "Остаток от деления не всех кодов на производящий многочлен = 0")

print("\nДемонстрация цикличности кода")
flag = True
for code in code_table:
    new = code[-1:] + code[:-1]
    if new not in code_table:
        flag = False
        break
print("Все коды после перестановки входят в множество кодовых слов" if flag else "Не все коды после перестановки входят в множество кодовых слов")
print()

'''Код может исправить одну и обнаружить две ошибки. Значит если в полученном сообщении будет 2 ошибки, то они будут обнаружены, но не будут исправлены.'''
sent_message = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
change_message = polynomial_multiplication(sent_message, [1, 0, 0, 0])
q, r = Module_two_division.poly_divmod(change_message, p)
if r != [0]:
    if len(r) < 4:
        for i in range(4 - len(r)):
            r.insert(0, 0)
    sent_message.extend(r)
'''11 первых бит - информационные. Последние 4 - контрольные'''
q, r = Module_two_division.poly_divmod(sent_message, p)
print("Отправленное сообщение ", sent_message if r == [0] else "Error")
message_with_double_error = sent_message.copy()

count = 0
for i in range(len(sent_message)):
    flag = bool(random.getrandbits(1))
    if flag:
        count += 1
        if count <= 2:
            message_with_double_error[i] = 0 if sent_message[i] == 1 else 1
        else:
            break
print("Сообщение с ошибками ", message_with_double_error)
q, r = Module_two_division.poly_divmod(message_with_double_error, p)
print("Есть ошибка" if r != [0] else "Ошибок не обнаружено")
error_vector = [0 if sent_message[i] == message_with_double_error[i] else 1 for i in range(len(sent_message)) ]
print("Вектор ошибок ", error_vector)
