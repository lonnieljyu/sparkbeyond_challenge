import sys
import psycopg2
import csv
from constants import HOST_NAME, DB_NAME, USER_NAME

"""
write_day_summaries_to_csv.py
usage: python write_day_summaries_to_csv [country_name] [year] [output_file_path].csv

Writes NOAA GSOD day summaries, queried from PostgreSQL by country name and year, into a CSV file.

- Lonnie Yu
"""


def get_query_results_by_country(connection, country_name, year):
    """
    Executes and returns the query result.
    The query selects GSOD day summaries in the given year joined with station data for all stations in the given
    country.

    :param connection: Psycopg2 connection to PostgreSQL
    :type connection: psycopg2.connection
    :param country_name: Country name queried by
    :type country_name: string
    :param year: Year queried by
    :type year: string
    :return rows: The query results as a list of rows where each row is a tuple
    :rtype rows: list()
    """

    rows = [
        ("STN", "WBAN", "YEARMODA", "TEMP", "TEMP_Count", "DEWP", "DEWP_Count",
         "SLP", "SLP_Count", "STP", "STP_Count", "VISIB", "VISIB_Count",
         "WDSP", "WDSP_Count", "MXSPD", "GUST", "MAX", "MAX_Flag", "MIN", "MIN_Flag",
         "PRCP", "PRCP_Flag", "SNDP", "FRSHTT",
         "STATION_NAME", "CTRY", "ST", "ICAO", "LAT", "LON", "ELEV(M)", "BEGIN", "END")
    ]

    query = '''
        Select 
            "STN", ds."WBAN", "YEARMODA", "TEMP", "TEMP_Count", "DEWP", "DEWP_Count",
            "SLP", "SLP_Count", "STP", "STP_Count", "VISIB", "VISIB_Count", 
            "WDSP", "WDSP_Count", "MXSPD", "GUST", "MAX", "MAX_Flag", "MIN", "MIN_Flag", 
            "PRCP", "PRCP_Flag", "SNDP", "FRSHTT", 
            "STATION_NAME", "CTRY", "ST", "ICAO", "LAT", "LON", "ELEV(M)", "BEGIN", "END"
        From day_summaries ds
        Join (Select 
                "USAF", "WBAN", "STATION_NAME", "CTRY", "ST", "ICAO", "LAT", "LON", "ELEV(M)", 
                "BEGIN", "END"
            From stations
            Where "CTRY" in
                (Select "FIPS_ID"
                From countries
                Where "COUNTRY_NAME" ~* '.*''' + country_name + '''.*'
                )
            ) s
            On s."USAF" = ds."STN" AND s."WBAN" = ds."WBAN"
        Where "YEARMODA" Like \'''' + year + '''%'
    '''

    cursor = connection.cursor()
    cursor.execute(query)
    rows.extend(cursor.fetchall())
    return rows


def write_rows_to_csv(rows, csv_file_path):
    """
    Formats and writes the rows to the CSV file.

    :param rows: List of tuples where each tuple is a row
    :type rows: list()
    :param csv_file_path: The CSV file path
    :type csv_file_path: string
    """

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in rows:
            csv_writer.writerow((str(x).strip() for x in row))


def write_day_summaries_to_csv(country_name, year, csv_file_path):
    """
    Connects to and queries by country name from PostgreSQL.
    Writes query results to the CSV file.

    :param country_name: Country name to be queried by
    :type country_name: string
    :param year: Year to be queried by
    :type year: string
    :param csv_file_path: The CSV file path
    :type csv_file_path: string
    """

    try:
        connection = psycopg2.connect(host=HOST_NAME, dbname=DB_NAME, user=USER_NAME)
    except Exception as e:
        print('Unable to connect to database:\n' + str(e))
        return

    write_rows_to_csv(get_query_results_by_country(connection, country_name, year), csv_file_path)
    connection.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('usage: python write_day_summaries_to_csv [country_name] [year] [output_file_path].csv')
    else:
        write_day_summaries_to_csv(sys.argv[1], sys.argv[2], sys.argv[3])
