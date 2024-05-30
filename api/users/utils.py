from cryptography.fernet import Fernet
from api.config import ENCRYPT_KEY


def encrypt_code(code: str):
    cipher_suite = Fernet(ENCRYPT_KEY.encode('utf-8'))
    return cipher_suite.encrypt(code.encode('utf-8')).decode('utf-8')


def decrypt_code(code: str):
    cipher_suite = Fernet(ENCRYPT_KEY.encode('utf-8'))
    return cipher_suite.decrypt(code.encode('utf-8')).decode('utf-8')

