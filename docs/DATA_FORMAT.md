# Data Format Documentation

This document describes the expected data formats for the air transport network analysis.

## Airport Data

Expected format for airport data (`data/raw/airports.csv`):

| Column | Type | Description |
|--------|------|-------------|
| airport_id | int | Unique identifier for the airport |
| name | string | Airport name |
| city | string | City where airport is located |
| country | string | Country code |
| iata | string | IATA code (3 letters) |
| icao | string | ICAO code (4 letters) |
| latitude | float | Latitude coordinate |
| longitude | float | Longitude coordinate |
| altitude | float | Altitude in feet |

## Route Data

Expected format for route data (`data/raw/routes.csv`):

| Column | Type | Description |
|--------|------|-------------|
| airline | string | Airline code |
| source_airport | string | Source airport IATA/ICAO code |
| destination_airport | string | Destination airport IATA/ICAO code |
| codeshare | string | Codeshare flag (Y/N) |
| stops | int | Number of stops |
| equipment | string | Aircraft type |

## Flight Data (Optional)

Expected format for flight frequency data (`data/raw/flights.csv`):

| Column | Type | Description |
|--------|------|-------------|
| source | string | Source airport code |
| destination | string | Destination airport code |
| frequency | int | Number of flights per week/month |
| passengers | int | Estimated passenger volume |

## Data Sources

Potential data sources for air transport networks:

1. **OpenFlights**: Open-source airport and route data
   - URL: https://openflights.org/data.html
   
2. **OurAirports**: Airport database
   - URL: https://ourairports.com/data/

3. **Bureau of Transportation Statistics**: US flight data
   - URL: https://www.transtats.bts.gov/

## Data Preprocessing

Place your raw data files in the `data/raw/` directory. Processed data will be saved to `data/processed/` after running the preprocessing steps in the notebooks.

### Preprocessing Steps

1. **Data Cleaning**
   - Remove entries with missing coordinates
   - Validate airport codes
   - Handle duplicate routes

2. **Data Transformation**
   - Convert to appropriate data types
   - Create edge lists from route data
   - Aggregate flight frequencies

3. **Network Construction**
   - Create nodes from airport data
   - Create edges from route data
   - Add weights based on flight frequency or distance
