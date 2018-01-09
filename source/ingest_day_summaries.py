import psycopg2
from glob import glob
from io import StringIO
from constants import HOST_NAME, DB_NAME, USER_NAME, TABLE_NAME, \
    DAY_SUMMARIES_PATH, DAY_SUMMARY_FILE_EXT, DAY_SUMMARY_FIELD_RANGES

"""
ingest_day_summaries.py
Usage: python ingest_day_summaries.py

Ingests NOAA GSOD day summaries data into PostgreSQL.

- Lonnie Yu
"""


def get_formatted_day_summaries(file_path):
    """
    Parses day summaries file into formatted data.
    Assumes headers as first row and ignores it.

    :param file_path: Day summaries file path.
    :type file_path: string
    :return rows: Formatted day summaries data.
    :rtype rows: string
    """

    rows = list()
    with open(file_path, 'r') as file:
        file.readline()
        for line in file:
            values = list()
            for start, end in DAY_SUMMARY_FIELD_RANGES:
                values.append(line[start - 1:end])
            rows.append('\t'.join(values))
    rows = '\n'.join(rows)
    return rows


def get_day_summaries_stream():
    """
    Creates day summaries data stream.

    :return string_buffer: Day summaries data stream
    :rtype string_buffer: StringIO
    """

    string_buffer = StringIO()
    file_paths = glob(DAY_SUMMARIES_PATH + '/*.' + DAY_SUMMARY_FILE_EXT)
    for file_path in file_paths:
        string_buffer.write(get_formatted_day_summaries(file_path) + '\n')
    string_buffer.seek(0)
    return string_buffer


def ingest_day_summaries():
    """
    Connects to and ingests day summaries into PostgreSQL.
    """

    try:
        connection = psycopg2.connect(host=HOST_NAME, dbname=DB_NAME, user=USER_NAME)
    except Exception as e:
        print('Unable to connect to database:\n' + str(e))
        return

    connection.cursor() \
        .copy_from(get_day_summaries_stream(), TABLE_NAME)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    ingest_day_summaries()
