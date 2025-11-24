from norman_utils_external.secure_random_bytes_generator import SecureRandomBytesGenerator


class SecureRandomIntGenerator:
    """
    Cryptographically secure random integer generator for producing uniformly
    distributed integers within a specified inclusive range.

    This generator uses `SecureRandomBytesGenerator` (ChaCha20-based) as its
    entropy source and applies *rejection sampling* to guarantee an unbiased
    distribution even when the range does not evenly divide the underlying
    byte space.

    **How It Works**

    - A stream of secure random bytes is generated using ChaCha20.
    - The random bytes are converted to an integer (`value`).
    - Values falling inside a “rejection zone”—which would cause modulo bias—
      are discarded.
    - The accepted value is reduced to the desired range and returned.

    **Attributes**

    - **lower_bound** (`int`)
      Inclusive minimum integer that may be returned.

    - **upper_bound** (`int`)
      Inclusive maximum integer that may be returned.

    - **range_size** (`int`)
      Size of the integer domain (`upper_bound - lower_bound + 1`).

    - **bits_needed** (`int`)
      Minimum number of bits required to represent all values in the range.

    - **bytes_needed** (`int`)
      Number of bytes needed to contain `bits_needed`.

    - **max_value** (`int`)
      Maximum integer representable by `bytes_needed` bytes.

    - **rejection_threshold** (`int`)
      Values ≥ this threshold are rejected to avoid modulo bias.
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

    def generate(self):
        """
        Generate a secure random integer within the configured range.

        Uses rejection sampling to ensure every integer in the range
        `[lower_bound, upper_bound]` has equal probability.

        **Returns**

        - **int** — A cryptographically secure uniformly distributed integer
          between `lower_bound` and `upper_bound` (inclusive).

        **Algorithm**

        1. Request `bytes_needed` secure random bytes.
        2. Convert bytes → integer (`value`).
        3. Reject the value if:
           ```
           value >= rejection_threshold
           ```
           to avoid modulo bias.
        4. Otherwise return:
           ```
           lower_bound + (value % range_size)
           ```

        **Example**
        ```python
        rng = SecureRandomIntGenerator(1, 100)
        result = rng.generate()   # secure random integer between 1 and 100
        ```
        """
        while True:
            random_bytes = self.entropy_source.next(self.bytes_needed)
            value = int.from_bytes(random_bytes, byteorder="big")

            if value < self.rejection_threshold:
                return self.lower_bound + (value % self.range_size)
