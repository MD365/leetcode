import binascii
import re
from Crypto.Cipher import AES
import base64
from Crypto import Random

AES_SECRET_KEY='B31F2A75FBF94099'
IV = '1234567890123456'.encode("utf-")

#PADDING算法
BS = AES.block_size
pad = lambda s:s+(BS-len(s)%BS) * chr(BS-len(s)%BS)
nupad = lambda s : s[0:-ord(s[-1])]


class AES_ENCRYPT:
    def __init__(self):
        self.key = AES_SECRET_KEY.encode("utf-8")

        self.mode = AES.MODE_CBC

    #加密函数
    def encrypt(self, text):

        cryptor = AES.new(self.key,self.mode,IV)
        self.ciphertext = cryptor.encrypt(pad(text.encode('utf8')))
        return base64.b64encode(self.ciphertext)
    #解密函数
    def decrypt(self,text):
        decode = base64.b64encode(text)
        cryptor = AES.new(self.key, self.mode,IV)
        plain_test = cryptor.decrypt(decode)
        return plain_test


def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    iv = Random.new().read(bs)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data))
    data = iv + data
    return (data)


def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return (data)
    unpad = lambda s: s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(data[bs:]))
    return (data)
class AESCBC:
    def __init__(self):
        self.key = '0123456789012345'.encode('utf-8')  # 定义key值
        self.mode = AES.MODE_CBC
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def encrypt(self,text):
        generator = AES.new(self.key,self.mode,IV)
        crypt = generator.encrypt(self.PADDING(text))
        crypted_str = binascii.b2a_hex(crypt)
        result = crypted_str.decode()
        return result

    def decrypt(self,text):
        generator = AES.new(self.key,self.mode, IV)
        text += (len(text)%4) * '='
        decrpyt_bytes = binascii.a2b_hex(text)
        meg = generator.decrypt(decrpyt_bytes)
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', meg.decode())
        except Exception:
            result = '解码失败，请重试!'
        return result



if __name__ == '__main__':
    aes = AES_ENCRYPT()

    to_encrypt = '12345'
    to_decrypt = '31f45bc15c28b3dffb7886d86ae0136d'
    (aes.encrypt(to_encrypt))


