from typing import Set


class FileTypeCategories:

    __SUPPORTED_IMAGE_ASSETS: Set[str] = {"jpg", "jpeg", "png", "webp"}
    __SUPPORTED_MODEL_ASSETS: Set[str] = {"jit", "pt"}

    __ZIP_BASED_TYPES: Set[str] = {"docx", "jar", "pt", "xlsx", "zip", "pptx", "odt", "ods", "odp"}
    __TEXT_BASED_TYPES: Set[str] = {"ass", "csv", "json", "srt", "txt", "utf8", "utf16", "utf32", "vtt", "xml"}
    __MATROSKA_TYPES: Set[str] = {"matroska", "mkv", "webm"}
    __OGG_TYPES: Set[str] = {"ogg", "opus", "vorbis"}

    __TYPE_ALIASES: dict[str, str] = {
        "jpg": "jpg",
        "jpeg": "jpg",
        "tif": "tif",
        "tiff": "tif",
        "htm": "html",
        "html": "html",
    }

    @classmethod
    def get_allowed_image_assets(cls):
        return cls.__SUPPORTED_IMAGE_ASSETS.copy()

    @classmethod
    def get_allowed_model_assets(cls):
        return cls.__SUPPORTED_MODEL_ASSETS.copy()

    @classmethod
    def get_allowed_assets(cls):
        return cls.__SUPPORTED_IMAGE_ASSETS | cls.__SUPPORTED_MODEL_ASSETS

    @classmethod
    def is_zip_based_type(cls, file_type: str):
        return file_type.lower() in cls.__ZIP_BASED_TYPES

    @classmethod
    def is_text_based_type(cls, file_type: str):
        return file_type.lower() in cls.__TEXT_BASED_TYPES

    @classmethod
    def is_matroska_type(cls, file_type: str):
        return file_type.lower() in cls.__MATROSKA_TYPES

    @classmethod
    def is_ogg_type(cls, file_type: str):
        return file_type.lower() in cls.__OGG_TYPES

    @classmethod
    def normalize_type(cls, file_type: str):
        return cls.__TYPE_ALIASES.get(file_type.lower(), file_type.lower())

    @classmethod
    def has_zip_based_type(cls, allowed_types: Set[str]):
        return any(cls.is_zip_based_type(t) for t in allowed_types)

    @classmethod
    def has_text_based_type(cls, allowed_types: Set[str]):
        return any(cls.is_text_based_type(t) for t in allowed_types)

    @classmethod
    def has_matroska_type(cls, allowed_types: Set[str]):
        return any(cls.is_matroska_type(t) for t in allowed_types)

    @classmethod
    def has_ogg_type(cls, allowed_types: Set[str]):
        return any(cls.is_ogg_type(t) for t in allowed_types)