import io
import os
from typing import Final

from norman_utils_external.singleton import Singleton


class FileUtils(metaclass=Singleton):
    """
    Utility class for performing file-related operations, including
    buffer-size detection, file type inference from binary headers,
    and UTF-8 detection.

    This class is implemented as a singleton to ensure consistent and
    efficient use across the system, especially for repetitive header
    inspections and file classification logic.

    **Constructor**

    ***__init__()***

    Initialize internal UTF-8 and UTF-16 byte-order marker tables used for
    text-encoding detection.

    This constructor is intentionally lightweight because the class is a
    singleton; instances are reused across the system to minimize repeated
    header-inspection setup.


    **Methods**
    """

    def __init__(self):
        self.__UTF8_BYTE_ORDER_MARKS: Final = ["efbbbf"]
        self.__UTF16_BYTE_ORDER_MARKS: Final = ["feff", "fffe"]  # Big endian & little endian

    @staticmethod
    def get_buffer_size(file_obj) -> int:
        """
        Determine the size (in bytes) of the given file-like object.

        Supports:
        - Standard file objects with a `fileno()`
        - In-memory `io.BytesIO` buffers

        **Parameters**

        - **file_obj**
          A file-like object. Must either:

              - Support `fileno()`
              - Be an instance of `io.BytesIO`

        **Returns**

        - **int** - Total number of bytes in the file or buffer.

        **Raises**

        - **ValueError** - If the object type is unsupported.
        """
        if hasattr(file_obj, "fileno"):
            return os.fstat(file_obj.fileno()).st_size
        if isinstance(file_obj, io.BytesIO):
            return file_obj.getbuffer().nbytes
        raise ValueError("Unsupported file object or operation")

    def get_file_type(self, file_path: str) -> tuple[str, str, str]:
        """
        Infer the file type by examining the first bytes of the file.

        **Parameters**

        - **file_path** (`str`)
          Path to the file to inspect.

        **Returns**

        - **tuple[str, str, str]**

              - Data modality (`"Audio"`, `"Image"`, `"Video"`, `"Text"`, `"File"`)
              - File extension (e.g., `"mp3"`, `"png"`, `"utf8"`, `"bin"`)
              - MIME type (e.g., `"audio/mpeg"`, `"image/png"`, `"application/octet-stream"`)
        """
        try:
            with open(file_path, "rb") as file:
                header = file.read(1024)
                # Reading 1024 bytes (instead of 128 or less) to improve detection accuracy
                # for unmarked UTF-8 files and formats lacking clear headers

        except IOError:
            return {
                "data_modality": "File",
                "data_encoding": "bin",
                "mime_type": "application/octet-stream",
                "file_extension": "bin",
                "Content-Type": "application/octet-stream"
            }
        return self.__get_file_type_from_header(header)

    def __get_file_type_from_header(self, header: bytes):
        hex_header = header.hex()

        if hex_header.startswith("494433"):
            data_modality, data_encoding, mime_type, file_extension = "Audio", "mp3", "audio/mpeg", "mp3"
        elif hex_header.startswith("504b0304"):
            data_modality, data_encoding, mime_type, file_extension = "File", "bin", "application/octet-stream", "bin"  # `.pt` files have a zip header
        elif hex_header.startswith("89504e47"):
            data_modality, data_encoding, mime_type, file_extension = "Image", "png", "image/png", "png"
        elif hex_header.startswith("ffd8ff"):
            data_modality, data_encoding, mime_type, file_extension = "Image", "jpg", "image/jpeg", "jpg"
        elif hex_header.startswith("fff1") or hex_header.startswith("fff9"):
            data_modality, data_encoding, mime_type, file_extension = "Audio", "aac", "audio/aac", "aac"
        elif hex_header.startswith("52494646") and "57415645" in hex_header:
            data_modality, data_encoding, mime_type, file_extension = "Audio", "wav", "audio/wav", "wav"
        elif hex_header.startswith("000000") and "66747970" in hex_header:
            data_modality, data_encoding, mime_type, file_extension = "Video", "mp4", "video/mp4", "mp4"
        elif self.__is_utf16(header):
            data_modality, data_encoding, mime_type, file_extension = "Text", "utf16", "text/plain", "txt"
        elif self.__is_utf8(header):
            data_modality, data_encoding, mime_type, file_extension = "Text", "utf8", "text/plain", "txt"
        else:
            data_modality, data_encoding, mime_type, file_extension = "File", "bin", "application/octet-stream", "bin"

        return {
            "data_modality": data_modality,
            "data_encoding": data_encoding,
            "mime_type": mime_type,
            "file_extension": file_extension,
            "Content-Type": mime_type  # S3 relies on Content-Type for proper file handling.
        }

    def __is_utf16(self, header: bytes):
        hex_header = header.hex()
        for bom in self.__UTF16_BYTE_ORDER_MARKS:
            if hex_header.startswith(bom):
                return True

        # Try to decode as UTF-16 (with BOM detection)
        try:
            header.decode("utf-16")
            return True
        except Exception:
            return False

    def __is_utf8(self, header: bytes):
        for bom in self.__UTF8_BYTE_ORDER_MARKS:
            if header.hex().startswith(bom):
                return True

        # Try to decode as UTF-8
        try:
            header.decode("utf-8")
            return True
        except UnicodeDecodeError:
            return False
