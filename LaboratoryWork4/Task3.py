import math

import Task1

Task1.statistics()

codes = dict()
with open('statistics_mono.txt', 'r') as f:
    counter = 0
    for line in f:
        key, value = line.split('\t')
        codes[key] = counter
        counter += 1
    f.close()
print(codes)
length = len(codes)

with open('text.txt', 'r') as f:
    last_read_symbol = f.read(1)
    end = False

    while True:
        if last_read_symbol == '' or last_read_symbol == '\n':
            break
        current_line = last_read_symbol
        longest_prefix = ''

        if current_line in list(codes.keys()):
            while current_line in list(codes.keys()):
                longest_prefix = current_line
                last_read_symbol = f.read(1)
                if last_read_symbol == '':
                    break
                counter += 1
                current_line += last_read_symbol


        if current_line not in list(codes.keys()):
            if len(longest_prefix) > 0:
                codes[current_line] = list(codes.keys()).index(longest_prefix)
            else:
                codes[current_line] = len(list(codes.keys()))

print(codes)

coded_text = [list(codes.values())[i] for i in range(length, len(list(codes.values())))]
print(coded_text)

bin_min_len = math.ceil(math.log(length, 2))

result = ''
for code in coded_text:
    if 0 <= code <= length - 1:
        print(format(code, f'#0{bin_min_len + 2}b')[2:], end='.')
        result += format(code, f'#0{bin_min_len + 2}b')[2:]
    else:
        print(bin(code)[2:], end='.')
        result += bin(code)[2:]

def LZW():
    with open('results_bites.txt', 'a', encoding='utf-8') as f:
        f.write("LZW: " + str(len(result)) + ' бит\n')
        f.close()

    with open('LZW.txt', 'w', encoding='utf-8') as f:
        f.write(result)
        f.close()