import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
from norman_utils_external.singleton import Singleton


class SecureRandomBytesGenerator(metaclass=Singleton):
    """
    Cryptographically secure pseudo-random byte generator using ChaCha20.

    This utility produces an arbitrary number of cryptographically strong
    random bytes, suitable for:

    - Nonces
    - Encryption keys
    - Session tokens
    - Salts
    - Any security-sensitive randomness

    The generator is implemented as a singleton so that the internal
    ChaCha20 stream cipher state is preserved across calls. This avoids
    reseeding and ensures consistent forward-secure random output.

    **Constructor**

    Initializes the internal ChaCha20 stream cipher using a randomly
    generated 256-bit key and 128-bit nonce. The cipher is kept as a
    persistent encryptor object so that successive calls to `next()`
    continue the stream, ensuring cryptographically strong forward-secure
    random output.

    **Methods**
    """

    def __init__(self):
        self.__seed_key = os.urandom(32)
        self.__seed_nonce = os.urandom(16)

        algorithm = algorithms.ChaCha20(self.__seed_key, self.__seed_nonce)
        cipher = Cipher(algorithm, mode=None, backend=default_backend())
        self.__stream = cipher.encryptor()

    def next(self, number_of_bytes: int) -> bytes:
        """
        Generate the next `number_of_bytes` pseudo-random bytes from the
        ChaCha20 stream.

        **Parameters**

        - **number_of_bytes** (`int`)
          Number of random bytes to produce. Must be a non-negative integer.

        **Returns**

        - **bytes** - A bytes object containing the requested number of
          cryptographically secure random bytes.
        """
        return self.__stream.update(b'\x00' * number_of_bytes)
