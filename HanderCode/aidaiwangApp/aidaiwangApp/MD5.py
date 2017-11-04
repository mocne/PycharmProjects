import hashlib
import random
import string
'''
while 1:
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    strs = hashlib.md5(salt.encode('gb2312'))
    md5str = 'EFC8E121352A1694056968B24DF3948B'
    if md5str == strs.hexdigest():
        print(salt)
'''
'''
# asd = 'a1111111'
# temp = hashlib.md5(asd.encode('gb2312'))
# print(temp.hexdigest())
'''


while 1:
    temp0 = 'a' + str(random.randint(1000000, 9999999))
    print(temp0)
    temp1 = hashlib.md5(temp0.encode('gb2312'))
    if temp1.hexdigest() == 'EFC8E121352A1694056968B24DF3948B':
        print('*************************************************', temp0)
        break