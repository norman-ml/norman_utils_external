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
