proportions = {
    '-': 0,
    'a': 0.1,
    'b': 0.2,
    'c': 0.25,
    'd': 0.8,
    'e': 0.9,
    'f': 1
}
st = 'aecdfb'


def arithmetical_coding(start: float, end: float, num: int):
    global st
    
    alphabet = tuple(proportions.keys())
    symb = st[num]
    presymb = alphabet[alphabet.index(symb) - 1]
    cut_len = subtraction_with_round(end, start)

    start_new = multiply_with_round(proportions[presymb], cut_len) + start
    end_new = multiply_with_round(proportions[symb], cut_len)  + start
    
    return (start_new, end_new)
    


def count_dot_after(n: float) -> int:
    s = str(n)
    return (abs(s.find('.') - len(s)) - 1)


def multiply_with_round(n: float, m: float) -> float:
    n_dot_after = count_dot_after(n)
    m_dot_after = count_dot_after(m)

    return round(n * m, n_dot_after+m_dot_after)


def subtraction_with_round(n: float, m: float) -> float:
    n_dot_after = count_dot_after(n)
    m_dot_after = count_dot_after(m)

    return round(n - m, max(n_dot_after, m_dot_after))


res = (0, 1)
for i in range(len(st)):
    res = arithmetical_coding(res[0], res[1], i)


print(res)