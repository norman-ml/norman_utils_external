import uuid


# Recommended reading:
# https://dev.mysql.com/blog-archive/mysql-8-0-uuid-support/
# https://dev.mysql.com/blog-archive/storing-uuid-values-in-mysql-tables/
# sequential uuid. see https://stackoverflow.com/questions/1785503/when-should-i-use-uuid-uuid1-vs-uuid-uuid4-in-python
class UUIDUtils:
    @staticmethod
    def optimized_unique_id(unique_id = None):
        if unique_id is None:
            unique_id = uuid.uuid1()

        original_bytes = unique_id.bytes
        reordered_bytes = original_bytes[6:8] + original_bytes[4:6] + original_bytes[0:4] + original_bytes[8:16]

        return reordered_bytes

    @staticmethod
    def bytes_to_int(id_bytes: bytes):
        return int.from_bytes(id_bytes, byteorder="big")

    @staticmethod
    def int_to_bytes(id_int: int):
        return id_int.to_bytes(16, byteorder="big")

    @staticmethod
    def bytes_to_str_id(id_bytes: bytes):
        return str(UUIDUtils.bytes_to_int(id_bytes))

    @staticmethod
    def str_id_to_bytes(id_str: str):
        return UUIDUtils.int_to_bytes(int(id_str))