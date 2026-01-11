import filetype

from norman_utils_external.signature_modality_mapping import SignatureModalityMapping


class FileSanitizer:
    MIN_BYTES_FOR_DETECTION = 261
    TEXT_MODALITY = "Text"

    @classmethod
    def sanitize(cls, file_extension: str, required_modality: str):
        if file_extension not in SignatureModalityMapping.Encoding_Map:
            raise ValueError("File type is not supported.")

        data_modality = SignatureModalityMapping.Encoding_Map[file_extension]
        if data_modality != required_modality:
            raise ValueError("File modality does not match the expected modality.")

    @classmethod
    def get_file_extension(cls, file_content: bytes, required_modality: str = None):
        if required_modality == cls.TEXT_MODALITY:
            try:
                file_content.decode('utf-8')
                return "txt"
            except UnicodeDecodeError:
                raise ValueError("File content is not valid UTF-8 text.")

        if len(file_content) < cls.MIN_BYTES_FOR_DETECTION:
            raise ValueError("File content too short to validate.")

        file_type = filetype.guess(file_content)
        if file_type is None:
            raise ValueError("Unsupported file type - no matching signature found.")

        return file_type.extension
