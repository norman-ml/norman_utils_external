import filetype


class FileTypeDetector:

    MIN_BYTES_FOR_DETECTION = 261

    @classmethod
    def detect(cls, file_bytes: bytes):
        kind = filetype.guess(file_bytes)
        return kind.extension if kind else None

    @classmethod
    def is_image(cls, file_bytes: bytes):
        return filetype.is_image(file_bytes)

    @classmethod
    def is_video(cls, file_bytes: bytes):
        return filetype.is_video(file_bytes)

    @classmethod
    def is_audio(cls, file_bytes: bytes):
        return filetype.is_audio(file_bytes)

    @classmethod
    def is_archive(cls, file_bytes: bytes):
        return filetype.is_archive(file_bytes)