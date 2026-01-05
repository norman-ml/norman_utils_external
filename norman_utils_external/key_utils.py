import base64
import hashlib
import json

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers

class KeyUtils:
    @staticmethod
    def jwks_to_public_key(jwks: list[dict]) -> str:
        jwk = jwks[0]

        modulus_bytes = jwk.get("n")
        exponent_bytes = jwk.get("e")

        modulus = int.from_bytes(KeyUtils.decode_base64url(modulus_bytes), byteorder='big')
        exponent = int.from_bytes(KeyUtils.decode_base64url(exponent_bytes), byteorder='big')

        public_numbers = RSAPublicNumbers(exponent, modulus)
        public_key = public_numbers.public_key(default_backend())

        public_key_pem_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        pem_public_key = public_key_pem_bytes.decode('utf-8')

        return pem_public_key

    @staticmethod
    def public_key_to_jwk_list(public_key_pem: str) -> list[dict]:
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        public_numbers = public_key.public_numbers()

        modulus = public_numbers.n
        exponent = public_numbers.e

        modulus_bytes = modulus.to_bytes((modulus.bit_length() + 7) // 8, byteorder="big")
        exponent_bytes = exponent.to_bytes((exponent.bit_length() + 7) // 8, byteorder="big")

        encoded_modulus = base64.urlsafe_b64encode(modulus_bytes).rstrip(b"=").decode("utf-8")
        encoded_exponent = base64.urlsafe_b64encode(exponent_bytes).rstrip(b"=").decode("utf-8")

        thumbprint_json = json.dumps(
            {"kty": "RSA", "n": encoded_modulus, "e": encoded_exponent},
            separators=(",", ":"),
            sort_keys=True
        )

        thumbprint_bytes = thumbprint_json.encode("utf-8")
        thumbprint_digest = hashlib.sha256(thumbprint_bytes).digest()
        key_id = base64.urlsafe_b64encode(thumbprint_digest).rstrip(b"=").decode("utf-8")

        jwk = {
            "kty" : "RSA",
            "kid" : key_id,
            "use" : "sig",
            "alg" : "RS256",
            "n" : encoded_modulus,
            "e" : encoded_exponent
        }

        jwk_list = [jwk]
        return jwk_list

    @staticmethod
    def decode_base64url(data: str) -> bytes:
        padding = 4 - len(data) % 4
        if padding != 4:
            data += '=' * padding
        return base64.urlsafe_b64decode(data)
