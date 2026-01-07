import filetype

from norman_utils_external.signature_modality_mapping import SignatureModalityMapping


class FileSanitizer:
    # The number of bytes required by filetype package for type resolving
    MIN_BYTES_FOR_DETECTION = 261

    @classmethod
    def sanitize(cls, detected_type: str, required_modality: str):
        if SignatureModalityMapping.Encoding_Map.get(detected_type) != required_modality:
            raise ValueError("file type is not approved.")

    @classmethod
    def validate_file_bytes(cls, file_content: bytes):
        if len(file_content) < cls.MIN_BYTES_FOR_DETECTION:
            raise ValueError("File content too short to validate.")

        file_type = filetype.guess(file_content)
        file_extension = file_type.extension

        if file_extension is None:
            raise ValueError("Unsupported file type - no matching signature found.")

        return file_extension
