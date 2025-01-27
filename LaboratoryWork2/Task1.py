alphabet = 'ЧЕРЕСПОЛОСИЦА'
words_len = 6

words = set()

for a in range(len(alphabet)):
    if a != len(alphabet) - 1:
        remain1 = alphabet[:a] + alphabet[a+1:]
    else:
        remain1 = alphabet[:a]

    for b in range(len(remain1)):
        if b != len(remain1) - 1:
            remain2 = remain1[:b] + remain1[b+1:]
        else:
            remain2 = remain1[:b]

        for c in range(len(remain2)):
            if c != len(remain2) - 1:
                remain3 = remain2[:c] + remain2[c+1:]
            else:
                remain3 = remain2[:c]

            for d in range(len(remain3)):
                if d != len(remain3) - 1:
                    remain4 = remain3[:d] + remain3[d+1:]
                else:
                    remain4 = remain4[:d]

                for e in range(len(remain4)):
                    if e != len(remain4) - 1:
                        remain5 = remain4[:e] + remain4[e+1:]
                    else:
                        remain5 = remain1[:e]

                    for f in range(len(remain5)):
                        word = alphabet[a] + remain1[b] + remain2[c] + remain3[d] + remain4[e] + remain5[f] #+ remain6[g]
                        words.add(word)                          
print(len(words))