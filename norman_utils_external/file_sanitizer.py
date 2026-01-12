from norman_utils_external.file_utils import FileUtils
from norman_utils_external.signature_modality_mapping import SignatureModalityMapping
from norman_utils_external.singleton import Singleton


class FileSanitizer(metaclass=Singleton):
    def __init__(self):
        self.__file_utils = FileUtils()

    def sanitize(self, file_extension: str, required_modality: str):
        if file_extension not in SignatureModalityMapping.Encoding_Map:
            raise ValueError("File type is not supported.")

        data_modality = SignatureModalityMapping.Encoding_Map[file_extension]
        if data_modality != required_modality:
            raise ValueError("File modality does not match the expected modality.")

