-- Table: public.countries

-- DROP TABLE public.countries;

CREATE TABLE public.countries
(
  "FIPS_ID" character(2) NOT NULL,
  "COUNTRY_NAME" character varying NOT NULL,
  CONSTRAINT countries_pkey PRIMARY KEY ("FIPS_ID")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.countries
  OWNER TO postgres;


-- Table: public.stations

-- DROP TABLE public.stations;

CREATE TABLE public.stations
(
  "USAF" integer NOT NULL,
  "WBAN" integer NOT NULL,
  "STATION_NAME" character varying NOT NULL,
  "CTRY" character varying NOT NULL,
  "ST" character varying NOT NULL,
  "ICAO" character varying NOT NULL,
  "LAT" character varying NOT NULL,
  "LON" character varying NOT NULL,
  "ELEV(M)" character varying NOT NULL,
  "BEGIN" character varying NOT NULL,
  "END" character varying NOT NULL,
  CONSTRAINT stations_pkey PRIMARY KEY ("USAF", "WBAN")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.stations
  OWNER TO postgres;
COMMENT ON COLUMN public.stations."WBAN" IS '
';


-- Table: public.day_summaries

-- DROP TABLE public.day_summaries;

CREATE TABLE public.day_summaries
(
  "STN" integer NOT NULL,
  "WBAN" integer NOT NULL,
  "YEARMODA" character varying NOT NULL,
  "TEMP" character varying NOT NULL,
  "TEMP_Count" integer NOT NULL,
  "DEWP" character varying NOT NULL,
  "DEWP_Count" integer NOT NULL,
  "SLP" character varying NOT NULL,
  "SLP_Count" integer NOT NULL,
  "STP" character varying NOT NULL,
  "STP_Count" integer NOT NULL,
  "VISIB" character varying NOT NULL,
  "VISIB_Count" integer NOT NULL,
  "WDSP" character varying NOT NULL,
  "WDSP_Count" integer NOT NULL,
  "MXSPD" character varying NOT NULL,
  "GUST" character varying NOT NULL,
  "MAX" character varying NOT NULL,
  "MAX_Flag" character varying NOT NULL,
  "MIN" character varying NOT NULL,
  "MIN_Flag" character varying NOT NULL,
  "PRCP" character varying NOT NULL,
  "PRCP_Flag" character varying NOT NULL,
  "SNDP" character varying NOT NULL,
  "FRSHTT" character varying NOT NULL,
  CONSTRAINT day_summaries_pkey PRIMARY KEY ("STN", "WBAN", "YEARMODA")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.day_summaries
  OWNER TO postgres;
