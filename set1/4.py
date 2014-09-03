#!/usr/bin/python

# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.


crypto = [line.strip() for line in open('data-4.txt')]
#crypto = [line.strip() for line in open('data-4-sample.txt')]

dcrypto = []

for line in crypto:
        dcrypto.append(line.decode('hex'))

# ETAOIN SHRDLU

dtable = []

#for key in range(2):
for key in range(256):
    decrypt = []
    for line in range(len(dcrypto)):
        decrypt.append([])
    for i in range(len(dcrypto)):
        score = 0
        for j in range(len(dcrypto[i])):
                letter = chr(ord(dcrypto[i][j]) ^ key )
                decrypt[i].append(letter)
                if letter.lower() == 'e':
                    score += .127
                elif letter.lower() == 't':
                    score += .091
                elif letter.lower() == 'a':
                    score += .082
                elif letter.lower() == 'o':
                    score += .075
                elif letter.lower() == 'i':
                    score += .070
                elif letter.lower() == 'n':
                    score += .067
                elif letter.lower() == 's':
                    score += .063
                elif letter.lower() == 'h':
                    score += 0.061
                elif letter.lower() == 'r':
                    score += 0.060
                elif letter.lower() == 'd':
                    score += 0.043
                elif letter.lower() == 'l':
                    score += 0.040
                elif letter.lower() == 'u':
                    score += 0.027
                else:
                   score += 0
        dtext = ''.join(decrypt[i]) 
        dtable.append((key, i, dtext, score))
        #print key, i, dtext, score


# Sorting the list based on the score
def dsu_zip(table):
    tmp = [(x[3], x) for x in table]
    tmp.sort()
    return [x[1] for x in tmp]

scored_table = dsu_zip(dtable)

for x in range(10):
    print scored_table.pop()
