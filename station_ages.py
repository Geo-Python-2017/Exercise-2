#!/usr/bin/env python3
'''Prints the years since an FMI observation station has begun operation.

Description:
    This script is only a test for a planned version that would read in station
    information from a file and allow users to get the operational ages of any
    observation station in the FMI network. Currently, the user should specify
    the desired station at the start of the script as input and the age is
    written to the screen as output.

Note:
    All of the stations in this test version of the script are in Helsinki, so
    "Helsinki" has been removed from the station name for simplicity.

Limitations:
    This code will not work if the station is not in list of station names.

Usage:
    ./station_ages.py

Author:
    David Whipp - 10.9.2017

Modified by:
    None
'''

# Create and fill lists of station names and starting years for observation
#
# NOTE: Long lines can be split into multiple lines using the "\" character.
#       Split lines can be indented freely
stationNames = ['Harmaja', 'Kaisaniemi', 'Kaivopuisto', 'Kumpula', 'lighthouse', \
                'Malmi airfield', 'Suomenlinna aaltopoiju', 'Vuosaari harbour']
stationStartYears = [1989, 1844, 1904, 2005, 2003, 1937, 2016, 2012]

# Set the selected station
selectedStation = 1

# Find location of selected station
stationIndex = stationNames.index(selectedStation)

# Calculate operational years
stationYears = 2017 - stationStartYears[selectedStation]

# Print station name and number of years of operation on screen
print("The Helsinki", selectedStation, "station has been operational for", \
      stationYears, "years.)
