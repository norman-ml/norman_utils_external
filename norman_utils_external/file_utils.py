import io
import os
from typing import Final

from norman_utils_external.singleton import Singleton


class FileUtils(metaclass=Singleton):
    def __init__(self):
        self.__UTF8_BYTE_ORDER_MARKS: Final = ["efbbbf"]
        self.__UTF16_BYTE_ORDER_MARKS: Final = ["feff", "fffe"]  # Big endian and little endian, respectively

    @staticmethod
    def get_buffer_size(file_obj):
        if isinstance(file_obj, io.BytesIO):
            return file_obj.getbuffer().nbytes
        elif hasattr(file_obj, "fileno"):
            return os.fstat(file_obj.fileno()).st_size
        else:
            raise ValueError("Unsupported file object or operation")

    def get_file_type(self, file_path: str):
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
        return self.get_file_type_from_header(header)

    def get_file_type_from_header(self, header: bytes):
        hex_header = header.hex()

        # Audio (alphabetical: aac, ac3, flac, mp3, opus, vorbis, wav)
        if hex_header.startswith("fff1") or hex_header.startswith("fff9"):  # aac
            data_modality, data_encoding, mime_type, file_extension = "Audio", "aac", "audio/aac", "aac"
        elif hex_header.startswith("0b77"):  # ac3 sync word
            data_modality, data_encoding, mime_type, file_extension = "Audio", "ac3", "audio/ac3", "ac3"
        elif hex_header.startswith("664c6143"):  # flac - "fLaC"
            data_modality, data_encoding, mime_type, file_extension = "Audio", "flac", "audio/flac", "flac"
        elif hex_header.startswith("494433"):  # mp3 - ID3 tag
            data_modality, data_encoding, mime_type, file_extension = "Audio", "mp3", "audio/mpeg", "mp3"
        elif hex_header.startswith("4f676753") and "4f70757348656164" in hex_header:  # opus - OggS + OpusHead
            data_modality, data_encoding, mime_type, file_extension = "Audio", "opus", "audio/opus", "opus"
        elif hex_header.startswith("4f676753") and "01766f72626973" in hex_header:  # vorbis - OggS + \x01vorbis
            data_modality, data_encoding, mime_type, file_extension = "Audio", "vorbis", "audio/vorbis", "ogg"
        elif hex_header.startswith("52494646") and "57415645" in hex_header:  # wav - RIFF + WAVE
            data_modality, data_encoding, mime_type, file_extension = "Audio", "wav", "audio/wav", "wav"

        # Image (alphabetical: jpg, png, webp)
        elif hex_header.startswith("ffd8ff"):  # jpg
            data_modality, data_encoding, mime_type, file_extension = "Image", "jpg", "image/jpeg", "jpg"
        elif hex_header.startswith("89504e47"):  # png
            data_modality, data_encoding, mime_type, file_extension = "Image", "png", "image/png", "png"
        elif hex_header.startswith("52494646") and "57454250" in hex_header:  # webp - RIFF + WEBP
            data_modality, data_encoding, mime_type, file_extension = "Image", "webp", "image/webp", "webp"

        # Video (alphabetical: avi, matroska, mov, mp4, ogg, webm)
        elif hex_header.startswith("52494646") and "41564920" in hex_header:  # avi - RIFF + AVI
            data_modality, data_encoding, mime_type, file_extension = "Video", "avi", "video/x-msvideo", "avi"
        elif hex_header.startswith("1a45dfa3") and "7765626d" not in hex_header:  # matroska - EBML without webm doctype
            data_modality, data_encoding, mime_type, file_extension = "Video", "matroska", "video/x-matroska", "mkv"
        elif hex_header.startswith("000000") and "6674797071742020" in hex_header:  # mov - ftyp qt (QuickTime)
            data_modality, data_encoding, mime_type, file_extension = "Video", "mov", "video/quicktime", "mov"
        elif hex_header.startswith("000000") and "66747970" in hex_header:  # mp4 - ftyp (mp4 and variants)
            data_modality, data_encoding, mime_type, file_extension = "Video", "mp4", "video/mp4", "mp4"
        elif hex_header.startswith("4f676753"):  # ogg - OggS (generic, no vorbis/opus detected)
            data_modality, data_encoding, mime_type, file_extension = "Video", "ogg", "video/ogg", "ogg"
        elif hex_header.startswith("1a45dfa3") and "7765626d" in hex_header:  # webm - EBML + webm doctype
            data_modality, data_encoding, mime_type, file_extension = "Video", "webm", "video/webm", "webm"

        # File (zip-based formats: jit, pt, zip - all return bin)
        elif hex_header.startswith("504b0304"):  # `.pt` files have a zip header
            data_modality, data_encoding, mime_type, file_extension = "File", "bin", "application/octet-stream", "bin"

        # Text (must be last - uses fallback decode detection)
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
