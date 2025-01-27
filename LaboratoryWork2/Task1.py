def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_permutations(word, length):
    from collections import Counter
    
    # Подсчет количества каждой буквы
    letter_count = Counter(word)
    total_letters = sum(letter_count.values())
    
    # Если длина больше общего количества букв, вернуть 0
    if length > total_letters:
        return 0
    
    # Считаем количество перестановок
    total_permutations = factorial(total_letters) // factorial(total_letters - length)
    
    for count in letter_count.values():
        total_permutations //= factorial(count)
    
    return total_permutations

word = "ЧЕРЕСПОЛОСИЦА"
length = 6
result = count_permutations(word, length)
print(f"Количество различных слов длиной {length}: {result}")
