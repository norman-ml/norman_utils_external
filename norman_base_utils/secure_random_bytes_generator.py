import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
from norman_base_utils.singleton import Singleton


class SecureRandomBytesGenerator(metaclass=Singleton):
    def __init__(self):
        self.seed_key = os.urandom(32)
        self.seed_nonce = os.urandom(16)

        algorithm = algorithms.ChaCha20(self.seed_key, self.seed_nonce)
        cipher = Cipher(algorithm, mode=None, backend=default_backend())
        self._stream = cipher.encryptor()

    def next(self, number_of_bytes: int):
        return self._stream.update(b'\x00' * number_of_bytes)
