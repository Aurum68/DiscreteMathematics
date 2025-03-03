import itertools

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
for i in range(100):
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
    for j in range(i + 1, 11):
        print(f"d({code_table[i]}, {code_table[j]}) = {code_distance(code_table[i], code_table[j])}")

print(f"\nКратность гарантированно исправляемых кодом ошибок = {(min_distance - 1) // 2 if min_distance % 2 == 1 else min_distance // 2}")
print(f"Кратность гарантированно обнаруживаемых кодом ошибок = {min_distance - 1}")