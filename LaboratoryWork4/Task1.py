import math
from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    f.close()
    # Подсчет частоты букв
    char_freq = Counter(text)

    # Подсчет частоты пар букв
    pair_freq = Counter([text[i:i + 2] for i in range(len(text) - 1)])

def statistics():
    global text, char_freq, pair_freq

    # Выведем 10 самых частых символов и 10 самых частых пар

    top_chars = char_freq.most_common(10)

    top_pairs = pair_freq.most_common(10)

    print(top_chars, top_pairs)


    with open('statistics_mono.txt', 'w', encoding='utf-8') as f:
        for k, v in char_freq.items():
            f.write(k + '\t' + str(v) + '\n')
        f.close()

    with open('statistics_double.txt', 'w', encoding='utf-8') as f:
        for k, v in pair_freq.items():
            f.write(k + '\t' + str(v) + '\n')
        f.close()


def Shennon():
    global text
    shennon_information = -sum([(char_freq[i]/len(text) * math.log2(char_freq[i]/len(text))) for i in char_freq])

    with open('results_bites.txt', 'w', encoding='utf-8') as f:
        f.write("По формуле Шеннона " + str(shennon_information) + ' бит\n')
        f.close()


def uniform_code():
    global text, char_freq
    original_size = sum(char_freq.values()) * 6
    with open('results_bites.txt', 'a', encoding='utf-8') as f:
        f.write("Равномерный код :" + str(original_size) + ' бит\n')
    return original_size
