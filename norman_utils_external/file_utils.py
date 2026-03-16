import io
import os
from typing import Final

from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality

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

    def get_representation_from_path(self, file_path: str):
        try:
            with open(file_path, "rb") as file:
                header = file.read(1024)
                # Reading 1024 bytes (instead of 128 or less) to improve detection accuracy
                # for unmarked UTF-8 files and formats lacking clear headers
        except IOError as e:
            return {
                "container_modality": ContainerModality.File,
                "container_encoding": ContainerEncoding.Bin,
                "mime-type": "application/octet-stream",
                # HTTP relies on a mime-type header for content type resolving.
                "Content-Type": "application/octet-stream"  # S3 relies on Content-Type for proper file handling.
            }

        return self.get_representation_from_header(header)

    def get_representation_from_header(self, header: bytes):
        hex_header = header.hex()

        # Audio (alphabetical: aac, ac3, flac, mp3, ogg, wav)
        if hex_header.startswith("fff1") or hex_header.startswith("fff9"):  # aac
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Aac, "audio/aac"
        # elif hex_header.startswith("0b77"):  # ac3 sync word
        #     container_modality, container_encoding, mime_type = ContainerModality.Audio, "ac3", "audio/ac3"
        elif hex_header.startswith("664c6143"):  # flac - "fLaC"
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Flac, "audio/flac"
        elif hex_header.startswith("494433"):  # mp3 - ID3 tag
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Mp3, "audio/mpeg"
        elif hex_header.startswith("4f676753") and "4f70757348656164" in hex_header:  # opus - OggS + OpusHead
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Ogg, "audio/opus"
        elif hex_header.startswith("4f676753") and "01766f72626973" in hex_header:  # vorbis - OggS + \x01vorbis
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Ogg, "audio/vorbis"
        elif hex_header.startswith("52494646") and "57415645" in hex_header:  # wav - RIFF + WAVE
            container_modality, container_encoding, mime_type = ContainerModality.Audio, ContainerEncoding.Wav, "audio/wav"

        # Image (alphabetical: jpg, png, webp)
        elif hex_header.startswith("ffd8ff"):  # jpg
            container_modality, container_encoding, mime_type = ContainerModality.Image, ContainerEncoding.Jpg, "image/jpeg"
        elif hex_header.startswith("89504e47"):  # png
            container_modality, container_encoding, mime_type = ContainerModality.Image, ContainerEncoding.Png, "image/png"
        elif hex_header.startswith("52494646") and "57454250" in hex_header:  # webp - RIFF + WEBP
            container_modality, container_encoding, mime_type = ContainerModality.Image, ContainerEncoding.WebP, "image/webp"

        # Video (alphabetical: avi, mkv, mov, mp4, ogg, webm)
        # elif hex_header.startswith("52494646") and "41564920" in hex_header:  # avi - RIFF + AVI
        #     container_modality, container_encoding, mime_type = ContainerModality.Video, "avi", "video/x-msvideo"
        elif hex_header.startswith("1a45dfa3") and "7765626d" not in hex_header:  # matroska - EBML without webm doctype
            container_modality, container_encoding, mime_type = ContainerModality.Video, ContainerEncoding.Mkv, "video/x-matroska"
        elif hex_header.startswith("000000") and "6674797071742020" in hex_header:  # mov - ftyp qt (QuickTime)
            container_modality, container_encoding, mime_type = ContainerModality.Video, ContainerEncoding.Mov, "video/quicktime"
        elif hex_header.startswith("000000") and "66747970" in hex_header:  # mp4 - ftyp (mp4 and variants)
            container_modality, container_encoding, mime_type = ContainerModality.Video, ContainerEncoding.Mp4, "video/mp4"
        elif hex_header.startswith("4f676753"):  # ogg - OggS (generic, no vorbis/opus detected)
            container_modality, container_encoding, mime_type = ContainerModality.Video, ContainerEncoding.Ogg, "video/ogg"
        elif hex_header.startswith("1a45dfa3") and "7765626d" in hex_header:  # webm - EBML + webm doctype
            container_modality, container_encoding, mime_type = ContainerModality.Video, ContainerEncoding.WebM, "video/webm"

        # File (zip-based formats: jit, pt, zip - all return bin)
        elif hex_header.startswith("504b0304"):  # `.pt` files have a zip header
            container_modality, container_encoding, mime_type = ContainerModality.File, ContainerEncoding.Zip, "application/octet-stream"

        # Text (must be last - uses fallback decode detection)
        elif self.__is_utf16(header):
            container_modality, container_encoding, mime_type = ContainerModality.Text, ContainerEncoding.Txt, "text/plain"
        elif self.__is_utf8(header):
            container_modality, container_encoding, mime_type = ContainerModality.Text, ContainerEncoding.Txt, "text/plain"
        else:
            container_modality, container_encoding, mime_type = ContainerModality.File, ContainerEncoding.Bin, "application/octet-stream"

        return {
            "container_modality": container_modality,
            "container_encoding": container_encoding,
            "mime-type": mime_type,  # HTTP relies on a mime-type header for content type resolving.
            "Content-Type": mime_type  # S3 relies on Content-Type for proper file handling.
        }

    def get_text_channel_encoding_from_path(self, file_path: str):
        try:
            with open(file_path, "rb") as file:
                header = file.read(1024)
                # Reading 1024 bytes (instead of 128 or less) to improve detection accuracy
                # for unmarked UTF-8 files and formats lacking clear headers
        except IOError as e:
            raise IOError("Failed to read bytes from provided file path") from e

        return self.get_text_channel_encoding_from_header(header)

    def get_text_channel_encoding_from_header(self, header: bytes):
        if self.__is_utf16(header):
            return "utf16"
        elif self.__is_utf8(header):
            return "utf8"
        else:
            raise ValueError("Could not determine text channel encoding from file path")

    def __is_utf16(self, header: bytes):
        hex_header = header.hex()
        for bom in self.__UTF16_BYTE_ORDER_MARKS:
            if hex_header.startswith(bom):
                return True

        # Try to decode as UTF-16 (with BOM detection)
        try:
            header.decode("utf-16")
            return True
        except Exception as e:
            return False

    def __is_utf8(self, header: bytes):
        for bom in self.__UTF8_BYTE_ORDER_MARKS:
            if header.hex().startswith(bom):
                return True

        # Try to decode as UTF-8
        try:
            header.decode("utf-8")
            return True
        except Exception as e:
            return False
