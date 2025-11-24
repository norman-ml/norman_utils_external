from datetime import datetime


class DateUtils:
    """
    Utility class providing helper methods for converting between
    `datetime` objects and formatted timestamp strings.

    Supports both custom formats and two built-in formats commonly used
    across the Norman platform:

    - **utc_format** — `"YYYY-MM-DD HH:MM:SS.ssssss"`
      Example: `1970-01-01 00:00:00.000000`

    - **iso_8061_format** — `"YYYY-MM-DDTHH:MM:SS.ssssss+ZZZZ"`
      Example: `1970-01-01T00:00:00.000000+0000`

    These utilities are typically used for serialization, logging,
    persistence, or API interchange where consistent timestamp formatting
    is required.

    **Attributes**

    - **utc_format** (`str`)
      Default UTC timestamp format used when no format is provided.

    - **iso_8061_format** (`str`)
      ISO-8601–compliant timestamp format including timezone offset.
    """

    utc_format = "%Y-%m-%d %H:%M:%S.%f"      # 1970-01-01 00:00:00.000000
    iso_8061_format = "%Y-%m-%dT%H:%M:%S.%f%z"  # 1970-01-01T00:00:00.000000+0000

    @staticmethod
    def datetime_to_string(date_time: datetime, date_format: str = None):
        """
        Convert a `datetime` object into a formatted timestamp string.

        **Parameters**

        - **date_time** (`datetime`)
          The datetime instance to convert.

        - **date_format** (`Optional[str]`)
          String format to use with `strftime`.
          If not provided, defaults to `DateUtils.utc_format`.

        **Returns**

        - **str** — The formatted timestamp string.

        **Example**
        ```python
        ts = DateUtils.datetime_to_string(datetime.utcnow())
        ```
        """
        if date_format is None:
            date_format = DateUtils.utc_format

        return datetime.strftime(date_time, date_format)

    @staticmethod
    def string_to_datetime(date_string: str, date_format: str = None):
        """
        Parse a formatted timestamp string and convert it into a `datetime`
        object.

        **Parameters**

        - **date_string** (`str`)
          Timestamp string to parse.

        - **date_format** (`Optional[str]`)
          Format string to interpret the timestamp.
          If not provided, defaults to `DateUtils.utc_format`.

        **Returns**

        - **datetime** — Parsed datetime instance.

        **Example**
        ```python
        dt = DateUtils.string_to_datetime("2024-01-01 00:00:00.000000")
        ```
        """
        if date_format is None:
            date_format = DateUtils.utc_format

        return datetime.strptime(date_string, date_format)

