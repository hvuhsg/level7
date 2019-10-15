from pyaes import AESModeOfOperationCTR
from random import seed, randint
from time import time
from base64 import b64encode


def get_seed():
    now = time()
    print(now)
    now = round(now, 4)
    return now


def set_seed(seed_number):
    seed(seed_number)


def create_key(seed_number):
    set_seed(seed_number)
    key = [chr(randint(0, 200)) for _ in range(12)]
    key = ''.join(key).encode()
    return key


def encrypt_message(key, message):
    aes = AESModeOfOperationCTR(key=key)
    return aes.encrypt(message)

def main():
    key = create_key(get_seed())
    message = b"<the link>"
    en_message = b64encode(encrypt_message(key, message))
    print(en_message)
main()
