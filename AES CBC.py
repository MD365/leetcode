import binascii
import re
from Crypto.Cipher import AES
import base64


AES_SECRET_KEY='B31F2A75FBF94099'

IV = '1234567890123456'

#PADDING算法
BS = len(AES_SECRET_KEY)
pad = lambda s:s+(BS-len(s)%BS) * chr(BS-len(s)%BS)
nupad = lambda s : s[0:-ord(s[-1])]


class AES_ENCRYPT:
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC