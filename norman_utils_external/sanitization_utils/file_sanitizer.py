from typing import Optional, Set

from norman_utils_external.sanitization_utils.file_type_categories import FileTypeCategories
from norman_utils_external.sanitization_utils.file_type_detector import FileTypeDetector


class FileSanitizer:

    MIN_BYTES_FOR_DETECTION = FileTypeDetector.MIN_BYTES_FOR_DETECTION

    @classmethod
    def sanitize_file_bytes(cls, file_content: bytes, allowed_file_types: Set[str]):
        if FileTypeCategories.has_text_based_type(allowed_file_types):
            return None

        if len(file_content) < cls.MIN_BYTES_FOR_DETECTION:
            raise ValueError(
                f"File content too short to validate. "
                f"File must be at least {cls.MIN_BYTES_FOR_DETECTION} bytes"
            )

        detected_type = FileTypeDetector.detect(file_content)

        if detected_type is None:
            raise ValueError(
                "Unsupported file type - no matching signature found. "
                "File type could not be determined from magic number"
            )

        if cls.__is_allowed_container_type(detected_type, allowed_file_types):
            return detected_type

        normalized_detected = FileTypeCategories.normalize_type(detected_type)
        normalized_allowed = {
            FileTypeCategories.normalize_type(ft) for ft in allowed_file_types
        }

        if normalized_detected not in normalized_allowed:
            raise ValueError(
                f"File type not allowed. "
                f"Detected file type '{detected_type}' is not in allowed types '{allowed_file_types}'"
            )

        return detected_type

    @classmethod
    def __is_allowed_container_type(cls, detected_type: str, allowed_file_types: Set[str]):
        if detected_type == "zip" and FileTypeCategories.has_zip_based_type(allowed_file_types):
            return True

        if detected_type == "webm" and FileTypeCategories.has_matroska_type(allowed_file_types):
            return True

        if detected_type == "ogg" and FileTypeCategories.has_ogg_type(allowed_file_types):
            return True

        return False