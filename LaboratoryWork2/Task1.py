import itertools

word = "ЧЕРЕСПОЛОСИЦА"
length = 6
perm = set(itertools.combinations(word, length))
print(perm)
print(f"Количество различных слов длиной {length}: {len(perm)}")

if __name__ == "__main__":
    pass
