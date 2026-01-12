from norman_utils_external.file_utils import FileUtils
from norman_utils_external.signature_modality_mapping import SignatureModalityMapping


class FileSanitizer:

    @classmethod
    def sanitize(cls, file_extension: str, required_modality: str):
        if file_extension not in SignatureModalityMapping.Encoding_Map:
            raise ValueError("File type is not supported.")

        data_modality = SignatureModalityMapping.Encoding_Map[file_extension]
        if data_modality != required_modality:
            raise ValueError("File modality does not match the expected modality.")

    @classmethod
    def get_file_extension(cls, file_content: bytes):
        file_utils = FileUtils()
        file_type = file_utils.get_file_type_from_bytes(file_content)
        return file_type["data_encoding"]
