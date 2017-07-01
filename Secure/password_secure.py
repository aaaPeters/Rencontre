from random import Random
import hashlib

class Password_Secure():
    @classmethod
    def create_salt(cls, length = 32):
        salt = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        len_chars = len(chars) - 1
        random = Random()
        for iterator in xrange(length):
            salt += chars[random.randint(0, len_chars)]
        return salt

    @classmethod
    def string_md5(cls, string):
        return hashlib.md5(string).hexdigest()






