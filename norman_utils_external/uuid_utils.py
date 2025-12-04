import uuid


# Recommended reading:
# https://dev.mysql.com/blog-archive/mysql-8-0-uuid-support/
# https://dev.mysql.com/blog-archive/storing-uuid-values-in-mysql-tables/
# sequential uuid. see https://stackoverflow.com/questions/1785503/when-should-i-use-uuid-uuid1-vs-uuid-uuid4-in-python
class UUIDUtils:
    """
    Utility class providing optimized UUID generation and conversions used
    across the Norman platform.

    This class focuses on:
    - Generating sequential (time-ordered) UUIDs optimized for MySQL indexing
    - Reordering UUID bytes for improved locality in B-tree indexes
    - Converting UUIDs between bytes, integers, and string representations

    **Methods**
    """

    @staticmethod
    def optimized_unique_id(unique_id=None) -> bytes:
        """
        Generate a sequential, index-optimized UUID in 16-byte binary form.

        If no UUID is provided, a new `uuid.uuid1()` is created.
        The raw bytes of the UUID are then *reordered* to move the timestamp
        portion to the beginning, improving MySQL insertion locality and
        reducing B-tree fragmentation.

        **Parameters**

        - **unique_id** (`uuid.UUID | None`)
          Optional existing UUID.
          If `None`, a new UUID1 is generated automatically.

        **Returns**

        - **bytes** — 16-byte reordered UUID suitable for database storage.

        **Reordering Format**

        Original UUID1 byte layout:
        ```
        time_low | time_mid | time_hi_version | clock_seq | node
        ```

        Reordered layout (timestamp first):
        ```
        bytes[6:8] + bytes[4:6] + bytes[0:4] + bytes[8:16]
        ```

        This produces IDs that grow in natural chronological order.
        """
        if unique_id is None:
            unique_id = uuid.uuid1()

        original_bytes = unique_id.bytes
        reordered_bytes = (
            original_bytes[6:8] +
            original_bytes[4:6] +
            original_bytes[0:4] +
            original_bytes[8:16]
        )

        return reordered_bytes

    @staticmethod
    def bytes_to_int(id_bytes: bytes) -> int:
        """
        Convert a 16-byte UUID representation into its integer form.

        **Parameters**
        - **id_bytes** (`bytes`)
          16-byte UUID.

        **Returns**
        - **int** — Integer representing the UUID.
        """
        return int.from_bytes(id_bytes, byteorder="big")

    @staticmethod
    def int_to_bytes(id_int: int) -> bytes:
        """
        Convert an integer UUID representation back into 16 bytes.

        **Parameters**
        - **id_int** (`int`)
          Integer UUID.

        **Returns**
        - **bytes** — 16-byte big-endian UUID.
        """
        return id_int.to_bytes(16, byteorder="big")

    @staticmethod
    def bytes_to_str_id(id_bytes: bytes) -> str:
        """
        Convert a 16-byte UUID into a decimal string representation.

        Useful for serializing integer-based UUIDs to JSON or logs.

        **Parameters**
        - **id_bytes** (`bytes`)
          16-byte UUID.

        **Returns**
        - **str** — Decimal string encoding of the UUID.
        """
        return str(UUIDUtils.bytes_to_int(id_bytes))

    @staticmethod
    def str_id_to_bytes(id_str: str) -> bytes:
        """
        Convert a decimal UUID string back into 16-byte form.

        **Parameters**
        - **id_str** (`str`)
          Decimal string produced from `bytes_to_str_id()`.

        **Returns**
        - **bytes** — 16-byte UUID.
        """
        return UUIDUtils.int_to_bytes(int(id_str))
