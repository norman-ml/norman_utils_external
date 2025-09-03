from datetime import datetime

from norman_utils_external.date_utils import DateUtils


class JsonUtils:

    @staticmethod
    def default_serializer(obj):
        if isinstance(obj, datetime):
            return DateUtils.datetime_to_string(obj, DateUtils.iso_8061_format)
        else:
            return str(obj)
