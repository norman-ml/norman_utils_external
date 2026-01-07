from typing import Set
from .file_type_mapping import FileTypeMapping


class FileTypeHelpers:

    @staticmethod
    def get_allowed_image_assets():
        return FileTypeMapping.SUPPORTED_IMAGE_ASSETS.copy()

    @staticmethod
    def get_allowed_model_assets():
        return FileTypeMapping.SUPPORTED_MODEL_ASSETS.copy()

    @staticmethod
    def get_allowed_assets():
        return FileTypeMapping.SUPPORTED_IMAGE_ASSETS | FileTypeMapping.SUPPORTED_MODEL_ASSETS

    @staticmethod
    def is_zip_based_type(file_type: str):
        return file_type.lower() in FileTypeMapping.ZIP_BASED_TYPES

    @staticmethod
    def is_text_based_type(file_type: str):
        return file_type.lower() in FileTypeMapping.TEXT_BASED_TYPES

    @staticmethod
    def is_matroska_type(file_type: str):
        return file_type.lower() in FileTypeMapping.MATROSKA_TYPES

    @staticmethod
    def is_ogg_type(file_type: str):
        return file_type.lower() in FileTypeMapping.OGG_TYPES

    @staticmethod
    def normalize_type(file_type: str):
        return FileTypeMapping.TYPE_ALIASES.get(file_type.lower(), file_type.lower())

    @staticmethod
    def has_zip_based_type(allowed_types: Set[str]):
        return any(FileTypeHelpers.is_zip_based_type(t) for t in allowed_types)

    @staticmethod
    def has_text_based_type(allowed_types: Set[str]):
        return any(FileTypeHelpers.is_text_based_type(t) for t in allowed_types)

    @staticmethod
    def has_matroska_type(allowed_types: Set[str]):
        return any(FileTypeHelpers.is_matroska_type(t) for t in allowed_types)

    @staticmethod
    def has_ogg_type(allowed_types: Set[str]):
        return any(FileTypeHelpers.is_ogg_type(t) for t in allowed_types)
