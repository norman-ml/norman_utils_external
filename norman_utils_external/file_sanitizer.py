from norman_utils_external.encoding_combinations import EncodingCombinations
from norman_utils_external.file_utils import FileUtils
from norman_utils_external.singleton import Singleton


class FileSanitizer(metaclass=Singleton):
    def __init__(self):
        self.__file_utils = FileUtils()

    def sanitize(self, data_modality: str, required_modality: str):
        if data_modality not in EncodingCombinations.Combinations_Map:
            raise ValueError("File type is not supported")

        if data_modality != required_modality:
            raise ValueError("File modality does not match the expected modality")

