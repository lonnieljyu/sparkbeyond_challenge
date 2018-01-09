# SparkBeyond Challenge  
This challenge is for the data engineering role.  
This challenge provides a framework to ingest NOAA GSOD data into and query from PostgreSQL.  

# Requirements  
Python 3  
Psycopg2  
NOAA GSOD data  

# Data Source  
ftp://ftp.ncdc.noaa.gov/pub/data/gsod/  

# Workflow  
Source files are found in /source.  
The raw GSOD data must be placed in /data with subdirectories for each year, with the default data subdirectory being /data/gsod_2016 .  
initialize_gsod_db.sql initializes the GSOD tables in the PostgreSQL database.  
The countries and stations table values can be manually imported from country-list.txt or isd_history.csv or with your 
favorite import tool.  
constants.py contains PostgreSQL connection strings, directory locations, and the GSOD record format columns.  
ingest_day_summaries.py reads and inserts the GSOD data into the day_summaries table.  
write_day_summaries_to_csv.py queries the GSOD data by country and year and writes the results to a CSV file.  
