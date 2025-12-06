from norman_utils_external.secure_random_bytes_generator import SecureRandomBytesGenerator


class SecureRandomIntGenerator:
    """
    Cryptographically secure random integer generator for producing uniformly
    distributed integers within a specified inclusive range.

    This generator uses `SecureRandomBytesGenerator` (ChaCha20-based) as its
    entropy source and applies *rejection sampling* to guarantee an unbiased
    distribution even when the range does not evenly divide the underlying
    byte space.

    **Methods**
    """

    def __init__(self, lower_bound: int, upper_bound: int):
        if lower_bound >= upper_bound:
            raise ValueError("lower bound must be smaller then upper bound")

        self.entropy_source = SecureRandomBytesGenerator()

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.range_size = upper_bound - lower_bound + 1

        self.bits_needed = self.range_size.bit_length()
        self.bytes_needed = (self.bits_needed + 7) // 8
        self.max_value = 1 << (self.bytes_needed * 8)

        self.rejection_threshold = self.max_value - (self.max_value % self.range_size)

    def generate(self) -> int:
        """
        Generate a secure random integer within the configured range.

        Uses rejection sampling to ensure every integer in the range
        `[lower_bound, upper_bound]` has equal probability.

        **Returns**

        - **int** - A cryptographically secure uniformly distributed integer
          between `lower_bound` and `upper_bound` (inclusive).
        """
        while True:
            random_bytes = self.entropy_source.next(self.bytes_needed)
            value = int.from_bytes(random_bytes, byteorder="big")

            if value < self.rejection_threshold:
                return self.lower_bound + (value % self.range_size)
