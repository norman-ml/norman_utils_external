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

    **File Type Detection**
    The `get_file_type` method reads a portion of the file and determines
    its:
    - Data modality (Audio, Image, Text, File, Video)
    - Logical extension (e.g., `mp3`, `png`, `utf8`)
    - MIME type (e.g., `audio/mpeg`, `image/jpeg`, `text/plain`)

    It supports common formats used inside the Norman platform:
    - Audio: MP3, AAC, WAV
    - Image: PNG, JPG
    - Video: MP4
    - Text: UTF-8
    - Binary: fallback or unrecognized content
    """

    def __init__(self):
        self.__UTF8_BYTE_ORDER_MARKS: Final = ["efbbbf", "feff", "fffe"]

    @staticmethod
    def get_buffer_size(file_obj):
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

        - **int** — Total number of bytes in the file or buffer.

        **Raises**

        - **ValueError** — If the object type is unsupported.

        **Example**
        ```python
        with open("example.bin", "rb") as f:
            size = FileUtils.get_buffer_size(f)
        ```
        """
        if hasattr(file_obj, "fileno"):
            return os.fstat(file_obj.fileno()).st_size
        if isinstance(file_obj, io.BytesIO):
            return file_obj.getbuffer().nbytes
        raise ValueError("Unsupported file object or operation")

    def get_file_type(self, file_path: str):
        """
        Infer the file type by examining the first 1024 bytes of the file.

        This method attempts to classify the file into high-level categories
        such as audio, image, video, text, or generic binary, and returns
        a tuple containing:

        ```
        (data_modality, logical_extension, mime_type)
        ```

        **Parameters**

        - **file_path** (`str`)
          Path to the file to inspect.

        **Returns**

        - **tuple[str, str, str]** —
          - Data modality (`"Audio"`, `"Image"`, `"Video"`, `"Text"`, `"File"`)
          - Logical extension (e.g., `"mp3"`, `"png"`, `"utf8"`, `"bin"`)
          - MIME type (e.g., `"audio/mpeg"`, `"image/png"`, `"application/octet-stream"`)

        **Fallback Behavior**

        If the file cannot be opened (e.g., permissions error), returns:

        ```
        ("File", "bin", "application/octet-stream")
        ```
        """
        try:
            with open(file_path, "rb") as file:
                header = file.read(1024)
        except IOError:
            return "File", "bin", "application/octet-stream"
        return self.__get_file_type_from_header(header)

    def __get_file_type_from_header(self, header: bytes):
        """
        Internal helper that classifies a file based solely on its header bytes.

        Pattern-matches specific binary signatures (magic numbers) to known formats,
        including:

        - MP3 (`494433`)
        - ZIP/PT (`504b0304`)
        - PNG (`89504e47`)
        - JPG (`ffd8ff`)
        - AAC (`fff1` / `fff9`)
        - WAV (`52494646` + `57415645`)
        - MP4 (`...` + `66747970`)
        - UTF-8 (via BOM or decode test)

        **Returns**

        - **tuple[str, str, str]** —
          Same structure as `get_file_type`.
        """
        hex_header = header.hex()

        if hex_header.startswith("494433"):
            return "Audio", "mp3", "audio/mpeg"
        if hex_header.startswith("504b0304"):
            return "File", "bin", "application/octet-stream"  # .pt (PyTorch) files
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
        """
        Determine whether the given header bytes represent UTF-8 text.

        Detection strategy:

        1. Check for UTF-8 BOM signatures:
           - `EF BB BF`
           - `FE FF`
           - `FF FE`

        2. Attempt a UTF-8 decode. If decoding succeeds → treat as UTF-8.

        **Returns**

        - **bool** — `True` if the content appears to be UTF-8 text, else `False`.
        """
        for bom in self.__UTF8_BYTE_ORDER_MARKS:
            if header.hex().startswith(bom):
                return True
        try:
            header.decode("utf-8")
            return True
        except UnicodeDecodeError:
            return False
