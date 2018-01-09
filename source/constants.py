"""
constants.py

Connection strings and day summary field ranges.
The field ranges are one-based indices.

- Lonnie Yu
"""

HOST_NAME = 'localhost'
DB_NAME = 'gsod'
USER_NAME = 'postgres'
TABLE_NAME = 'day_summaries'
DAY_SUMMARIES_PATH = '../data/gsod_2016'
DAY_SUMMARY_FILE_EXT = 'op'
DAY_SUMMARY_FIELD_RANGES = [
    (  1,  6),      # STN
    (  8, 12),      # WBAN
    ( 15,  22),     # YEARMODA
    ( 25,  30),     # TEMP
    ( 32,  33),     # Count
    ( 36,  41),     # DEWP
    ( 43,  44),     # Count
    ( 47,  52),     # SLP
    ( 54,  55),     # Count
    ( 58,  63),     # STP
    ( 65,  66),     # Count
    ( 69,  73),     # VISIB
    ( 75,  76),     # Count
    ( 79,  83),     # WDSP
    ( 85,  86),     # Count
    ( 89,  93),     # MXSP
    ( 96, 100),     # GUST
    (103, 108),     # MAX
    (109, 109),     # Flag
    (111, 116),     # MIN
    (117, 117),     # Flag
    (119, 123),     # PRCP
    (124, 124),     # Flag
    (126, 130),     # SNDP
    (133, 138)      # FRSHTT
]
