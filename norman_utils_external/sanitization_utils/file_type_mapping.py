from typing import Set


class FileTypeMapping:

    SUPPORTED_IMAGE_ASSETS: Set[str] = {"jpg", "jpeg", "png", "webp"}
    SUPPORTED_MODEL_ASSETS: Set[str] = {"jit", "pt"}

    ZIP_BASED_TYPES: Set[str] = {"docx", "jar", "pt", "xlsx", "zip", "pptx", "odt", "ods", "odp"}
    TEXT_BASED_TYPES: Set[str] = {"ass", "csv", "json", "srt", "txt", "utf8", "utf16", "utf32", "vtt", "xml"}
    MATROSKA_TYPES: Set[str] = {"matroska", "mkv", "webm"}
    OGG_TYPES: Set[str] = {"ogg", "opus", "vorbis"}

    TYPE_ALIASES: dict[str, str] = {
        "jpg": "jpg",
        "jpeg": "jpg",
        "tif": "tif",
        "tiff": "tif",
        "htm": "html",
        "html": "html",
    }