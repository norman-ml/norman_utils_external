import base64


class EncodingUtils:
    @staticmethod
    def decode_base64url(data: str):
        padding = 4 - len(data) % 4
        if padding != 4:
            data += '=' * padding
        return base64.urlsafe_b64decode(data)
