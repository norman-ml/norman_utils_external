import filetype

from norman_utils_external.signature_modality_mapping import SignatureModalityMapping


class FileSanitizer:
    # The number of bytes required by filetype package for type resolving
    MIN_BYTES_FOR_DETECTION = 261

    @classmethod
    def sanitize(cls, file_extension: str, required_modality: str):
        if file_extension not in SignatureModalityMapping.Encoding_Map:
            raise KeyError("File type is not supported.")

        data_modality = SignatureModalityMapping.Encoding_Map[file_extension]
        if data_modality != required_modality:
            raise ValueError("File modality does not match the expected modality.")

    @classmethod
    def get_file_extension(cls, file_content: bytes):
        if len(file_content) < cls.MIN_BYTES_FOR_DETECTION:
            raise ValueError("File content too short to validate.")

        file_type = filetype.guess(file_content)
        file_extension = file_type.extension

        if file_extension is None:
            raise ValueError("Unsupported file type - no matching signature found.")

        return file_extension
