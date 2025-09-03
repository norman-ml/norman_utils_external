from norman_utils_external.secure_random_bytes_generator import SecureRandomBytesGenerator


class SecureRandomIntGenerator:
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
        while True:
            random_bytes = self.entropy_source.next(self.bytes_needed)
            value = int.from_bytes(random_bytes, byteorder="big")

            if value < self.rejection_threshold:
                return self.lower_bound + (value % self.range_size)
