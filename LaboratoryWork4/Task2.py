import heapq
import Task1

Task1.statistics()

# Класс для узлов дерева Хаффмана

class HuffmanNode:

    def __init__(self, char, freq):

        self.char = char

        self.freq = freq

        self.left = None

        self.right = None

    def __lt__(self, other):

        return self.freq < other.freq

# Построение дерева Хаффмана

def build_huffman_tree(freq_dict):

    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]

    heapq.heapify(heap)

    while len(heap) > 1:

        left = heapq.heappop(heap)

        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)

        merged.left = left

        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

# Генерация кодов Хаффмана

def generate_huffman_codes(node, prefix="", code_dict=dict()):

    if node is not None:

        if node.char is not None:

            code_dict[node.char] = prefix

        generate_huffman_codes(node.left, prefix + "0", code_dict)

        generate_huffman_codes(node.right, prefix + "1", code_dict)

    return code_dict

# Строим дерево и коды

with open('statistics_mono.txt', 'r', encoding='utf-8')as f:
    char_freq = dict()
    for line in f:
        k = line.split('\t')[0]
        v = int(line.split('\t')[1].strip())
        char_freq[k] = v
    f.close()

huffman_tree = build_huffman_tree(char_freq)

huffman_codes = generate_huffman_codes(huffman_tree)

# Вычисляем среднюю длину кодового слова

weighted_length = sum(len(huffman_codes[char]) * freq for char, freq in char_freq.items())

average_code_length = weighted_length / sum(char_freq.values())

# Вычисляем размер текста после кодирования

encoded_text_size = weighted_length  # В битах


# Выводим топ-10 закодированных символов

top_huffman_codes = sorted(huffman_codes.items(), key=lambda x: len(x[1]))[:10]

print(average_code_length, encoded_text_size, top_huffman_codes)

# Теперь можно рассчитать относительный процент сжатия.
# Процент сжатия:
# После кодирования Хаффмана размер текста уменьшился на 45.5% по сравнению с исходным 8-битным представлением ASCII.

Task1.Shennon()
original_size = Task1.uniform_code()

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("Код Хаффмана: " + str(encoded_text_size) + ' бит\n')
    f.close()

# Процент сжатия

compression_ratio = (1 - encoded_text_size / original_size) * 100

print(compression_ratio)

if __name__ == '__main__':
    pass