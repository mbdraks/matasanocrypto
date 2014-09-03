#!/usr/bin/python

# Fixed XOR

# Take 
# 1c0111001f010100061a024b53535009181c
# hex decode and then XOR it against
# 686974207468652062756c6c277320657965
# should produce
# 746865206b696420646f6e277420706c6179

key =    '1c0111001f010100061a024b53535009181c'
plain =  '686974207468652062756c6c277320657965'
crypto = '746865206b696420646f6e277420706c6179'

print 'key: %s' % key.decode('hex')
print 'plain: %s' % plain.decode('hex')
print 'crypto: %s' % crypto.decode('hex') 

# >>> dkey = key.decode('hex')
# >>> dkey
# '\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'
# 18 chars
# >>> 
# >>> dplain = plain.decode('hex')
# >>> dplain
# >>> "hit the bull's eye"
# 18 chars too

dkey = key.decode('hex')
dplain = plain.decode('hex')

dzip_kp = zip(dkey,dplain)

decrypt = []

for i in range(len(dzip_kp)):
   decrypt.append(chr(ord(dzip_kp[i][0]) ^ ord(dzip_kp[i][1])))

dec_join = ''.join(decrypt)

print 'decrypted: %s' % dec_join
print 'dec hex: %r' % dec_join.encode('hex')
print 'crypto: %r' % crypto
test = dec_join.encode('hex') == crypto
print "check: %r" % test 


# chr(65) == A
# ord('A') == 65

