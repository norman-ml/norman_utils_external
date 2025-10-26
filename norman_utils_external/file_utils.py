import io
import os
from typing import Final

from norman_utils_external.singleton import Singleton


class FileUtils(metaclass=Singleton):
    def __init__(self):
        self.__UTF8_BYTE_ORDER_MARKS: Final = ["efbbbf", "feff", "fffe"]

    def get_buffer_size(file_obj):
        if hasattr(file_obj, "fileno"):
            return os.fstat(file_obj.fileno()).st_size
        if isinstance(file_obj, io.BytesIO):
            return file_obj.getbuffer().nbytes
        raise ValueError("Unsupported file object or operation")

    def get_file_type(self, file_path: str):
        try:
            with open(file_path, "rb") as file:
                header = file.read(1024)
                # Reading 1024 bytes (instead of 128 or less) to improve detection accuracy
                # for unmarked UTF-8 files and formats lacking clear headers

        except IOError:
            return "File", "bin", "application/octet-stream"
        return self.__get_file_type_from_header(header)

    def __get_file_type_from_header(self, header: bytes):
        hex_header = header.hex()

        if hex_header.startswith("494433"):
            return "Audio", "mp3", "audio/mpeg"
        if hex_header.startswith("504b0304"):
            return "File", "bin", "application/octet-stream" # `.pt` files have a zip header
        if hex_header.startswith("89504e47"):
            return "Image", "png", "image/png"
        if hex_header.startswith("ffd8ff"):
            return "Image", "jpg", "image/jpeg"
        if hex_header.startswith("fff1") or hex_header.startswith("fff9"):
            return "Audio", "aac", "audio/aac"

        if hex_header.startswith("52494646") and "57415645" in hex_header:
            return "Audio", "wav", "audio/wav"
        if hex_header.startswith("000000") and "66747970" in hex_header:
            return "Video", "mp4", "video/mp4"

        if self.__is_utf8(header):
            return "Text", "utf8", "text/plain"

        return "File", "bin", "application/octet-stream"

    def __is_utf8(self, header: bytes):
        for bom in self.__UTF8_BYTE_ORDER_MARKS:
            if header.hex().startswith(bom):
                return True
        try:
            header.decode("utf-8")
            return True
        except UnicodeDecodeError:
            return False
