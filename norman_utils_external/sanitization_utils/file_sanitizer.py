import filetype

from norman_utils_external.signature_modality_mapping import SignatureModalityMapping


class FileSanitizer:

    # The number of bytes required by filetype package for type resolving
    MIN_BYTES_FOR_DETECTION = 261

    @classmethod
    def sanitize_file_bytes(cls, file_content: bytes, required_modality: str):

        if len(file_content) < cls.MIN_BYTES_FOR_DETECTION:
            raise ValueError(
                f"File content too short to validate. "
                f"File must be at least {cls.MIN_BYTES_FOR_DETECTION} bytes"
            )

        detected = filetype.guess(file_content)
        detected_type = detected.extension

        if detected_type is None:
            raise ValueError(
                "Unsupported file type - no matching signature found. "
                "File type could not be determined from magic number"
            )

        if SignatureModalityMapping.Encoding_Map(detected_type) != required_modality:
            raise ValueError(
                "file type is not approved. "
            )

