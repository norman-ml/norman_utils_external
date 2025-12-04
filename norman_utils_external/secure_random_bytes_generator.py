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

    - Implementation Details

        - A 32-byte random key and 16-byte random nonce are generated using
          `os.urandom()`.
        - ChaCha20 is initialized in *stream mode* using the key + nonce.
        - Each call to `next()` advances the cipher stream and returns the
          corresponding encrypted zero bytes as random output.

    **Attributes**

    - **seed_key** (`bytes`)
      A 32-byte cryptographic key generated via `os.urandom()` and used to
      initialize the ChaCha20 stream cipher.

    - **seed_nonce** (`bytes`)
      A 16-byte nonce generated via `os.urandom()` and paired with
      `seed_key` to initialize the ChaCha20 cipher.

    - **_stream** (`cryptography.hazmat.primitives.ciphers.base.CipherContext`)
      The internal ChaCha20 encryptor object. Acts as a forward-secure
      byte stream generator; its state advances with every call to `next()`.

    **Methods**
    """

    def __init__(self):
        self.seed_key = os.urandom(32)
        self.seed_nonce = os.urandom(16)

        algorithm = algorithms.ChaCha20(self.seed_key, self.seed_nonce)
        cipher = Cipher(algorithm, mode=None, backend=default_backend())
        self._stream = cipher.encryptor()

    def next(self, number_of_bytes: int) -> bytes:
        """
        Generate the next `number_of_bytes` pseudo-random bytes from the
        ChaCha20 stream.

        **Parameters**

        - **number_of_bytes** (`int`)
          Number of random bytes to produce. Must be a non-negative integer.

        **Returns**

        - **bytes** — A bytes object containing the requested number of
          cryptographically secure random bytes.
        """
        return self._stream.update(b'\x00' * number_of_bytes)
