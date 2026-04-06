import io
import os
from typing import Final

from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality
from norman_objects.shared.representation.file_representation import FileRepresentation

from norman_utils.singleton import Singleton


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
            return FileRepresentation(
                container_modality=ContainerModality.File,
                container_encoding=ContainerEncoding.Bin,
                mime_type="application/octet-stream"
            )

        return self.get_representation_from_header(header)

    def get_representation_from_header(self, header: bytes):
        hex_header = header.hex()

        # Audio (alphabetical: aac, ac3, flac, mp3, ogg, wav)
        if hex_header.startswith("fff1") or hex_header.startswith("fff9"):  # aac
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Aac,
                mime_type="audio/aac"
            )
        # elif hex_header.startswith("0b77"):  # ac3 sync word
        #     file_representation = FileRepresentation(
        #         container_modality=ContainerModality.Audio,
        #         container_encoding="ac3",
        #         mime_type="audio/ac3"
        #     )
        elif hex_header.startswith("664c6143"):  # flac - "fLaC"
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Flac,
                mime_type="audio/flac"
            )
        elif hex_header.startswith("494433"):  # mp3 - ID3 tag
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Mp3,
                mime_type="audio/mpeg"
            )
        elif hex_header.startswith("4f676753") and "4f70757348656164" in hex_header:  # opus - OggS + OpusHead
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Ogg,
                mime_type="audio/opus"
            )
        elif hex_header.startswith("4f676753") and "01766f72626973" in hex_header:  # vorbis - OggS + \x01vorbis
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Ogg,
                mime_type="audio/vorbis"
            )
        elif hex_header.startswith("52494646") and "57415645" in hex_header:  # wav - RIFF + WAVE
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Audio,
                container_encoding=ContainerEncoding.Wav,
                mime_type="audio/wav"
            )

        # Image (alphabetical: jpg, png, webp)
        elif hex_header.startswith("ffd8ff"):  # jpg
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Image,
                container_encoding=ContainerEncoding.Jpg,
                mime_type="image/jpeg"
            )
        elif hex_header.startswith("89504e47"):  # png
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Image,
                container_encoding=ContainerEncoding.Png,
                mime_type="image/png"
            )
        elif hex_header.startswith("52494646") and "57454250" in hex_header:  # webp - RIFF + WEBP
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Image,
                container_encoding=ContainerEncoding.WebP,
                mime_type="image/webp"
            )

        # Video (alphabetical: avi, mkv, mov, mp4, ogg, webm)
        # elif hex_header.startswith("52494646") and "41564920" in hex_header:  # avi - RIFF + AVI
        #     file_representation = FileRepresentation(
        #         container_modality=ContainerModality.Video,
        #         container_encoding="avi",
        #         mime_type="video/x-msvideo"
        #     )
        elif hex_header.startswith("1a45dfa3") and "7765626d" not in hex_header:  # matroska - EBML without webm doctype
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Video,
                container_encoding=ContainerEncoding.Mkv,
                mime_type="video/x-matroska"
            )
        elif hex_header.startswith("000000") and "6674797071742020" in hex_header:  # mov - ftyp qt (QuickTime)
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Video,
                container_encoding=ContainerEncoding.Mov,
                mime_type="video/quicktime"
            )
        elif hex_header.startswith("000000") and "66747970" in hex_header:  # mp4 - ftyp (mp4 and variants)
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Video,
                container_encoding=ContainerEncoding.Mp4,
                mime_type="video/mp4"
            )
        elif hex_header.startswith("4f676753"):  # ogg - OggS (generic, no vorbis/opus detected)
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Video,
                container_encoding=ContainerEncoding.Ogg,
                mime_type="video/ogg"
            )
        elif hex_header.startswith("1a45dfa3") and "7765626d" in hex_header:  # webm - EBML + webm doctype
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Video,
                container_encoding=ContainerEncoding.WebM,
                mime_type="video/webm"
            )

        # File (zip-based formats: jit, pt, zip - all return bin)
        elif hex_header.startswith("504b0304"):  # `.pt` files have a zip header
            file_representation = FileRepresentation(
                container_modality=ContainerModality.File,
                container_encoding=ContainerEncoding.Zip,
                mime_type="application/octet-stream"
            )

        # Text (must be last - uses fallback decode detection)
        elif self.__is_utf16(header):
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Text,
                container_encoding=ContainerEncoding.Txt,
                mime_type="text/plain"
            )
        elif self.__is_utf8(header):
            file_representation = FileRepresentation(
                container_modality=ContainerModality.Text,
                container_encoding=ContainerEncoding.Txt,
                mime_type="text/plain"
            )
        else:
            file_representation = FileRepresentation(
                container_modality=ContainerModality.File,
                container_encoding=ContainerEncoding.Bin,
                mime_type="application/octet-stream"
            )

        return file_representation

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
            return ChannelEncoding.Utf16
        elif self.__is_utf8(header):
            return ChannelEncoding.Utf8
        else:
            raise ValueError("Could not determine text channel encoding from file path")

    def __is_utf16(self, header: bytes):
        hex_header = header.hex()
        for bom in self.__UTF16_BYTE_ORDER_MARKS:
            if hex_header.startswith(bom):
                return True

        # Try to decode as UTF-16 (with BOM detection)
        try:
            encoding_name = ChannelEncoding.Utf16.value.lower()
            header.decode(encoding_name)
            return True
        except Exception as e:
            return False

    def __is_utf8(self, header: bytes):
        for bom in self.__UTF8_BYTE_ORDER_MARKS:
            if header.hex().startswith(bom):
                return True

        # Try to decode as UTF-8
        try:
            encoding_name = ChannelEncoding.Utf8.value.lower()
            header.decode(encoding_name)
            return True
        except Exception as e:
            return False
