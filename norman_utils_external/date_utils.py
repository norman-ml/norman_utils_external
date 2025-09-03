from datetime import datetime


class DateUtils:
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    utc_format = "%Y-%m-%d %H:%M:%S.%f"  # 1970-01-01 00:00:00.000000
    iso_8061_format = "%Y-%m-%dT%H:%M:%S.%f%z"  # 1970-01-01T00:00:00.000000+0000

    @staticmethod
    def datetime_to_string(date_time: datetime, date_format: str = None):
        if date_format is None:
            date_format = DateUtils.utc_format

        return datetime.strftime(date_time, date_format)

    @staticmethod
    def string_to_datetime(date_string: str, date_format: str = None):
        if date_format is None:
            date_format = DateUtils.utc_format

        return datetime.strptime(date_string, date_format)
