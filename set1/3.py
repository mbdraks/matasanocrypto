#!/usr/bin/python

# Single-byte XOR cipher
# Decode the XOR'ed message below, a single char is the key

crypto = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

dcrypto = crypto.decode('hex')

dtable = []

# ETAOIN SHRDLU

for key in range(256):
    decrypt = []
    score = 0
    for i in range(len(dcrypto)):
        letter = chr(ord(dcrypto[i]) ^ key )
        decrypt.append(letter)
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
    #print 'key: %s' % key
    dtext = ''.join(decrypt) 
    dtable.append((key, dtext, score))
    #print '%s: %s' % (key, dtext)


# Sorting the list based on the score
def dsu_zip(table):
    tmp = [(x[2], x) for x in table]
    tmp.sort()
    return [x[1] for x in tmp]

scored_table = dsu_zip(dtable)

for x in range(10):
    print scored_table.pop()
