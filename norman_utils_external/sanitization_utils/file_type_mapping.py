from typing import Set


class FileTypeMapping:

    SUPPORTED_IMAGE_ASSETS: Set[str] = {"jpg", "jpeg", "png", "webp"}
    SUPPORTED_MODEL_ASSETS: Set[str] = {"jit", "pt"}