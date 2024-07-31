#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

# =================updating the Airport codes in the google  sheet==========
data_manager = DataManager()
sheet_data = data_manager.getdata()
print(sheet_data)

flight_search = FlightSearch()

for city in sheet_data:
    if city["iataCodes"] == '':
        city["iataCodes"] = flight_search.get_destination_code(city['city'])
print(f"sheet_data:\n {sheet_data}")

data_manager.datarow = sheet_data
data_manager.edit_exiting_record()

# ============Set up the Flight Search ===
ORIGIN_CITY_IATA = 'LON'
flight_data = FlightData(None,None,None,None,None)

for destination in sheet_data:
    print(f"Getting flight for {destination['city']}...")
    flights = flight_search.check_flight(
        ORIGIN_CITY_IATA,destination['iataCode'],
        from_time=None,to_time=None
    )
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f"{destination['city']}: rs{cheapest_flight.price}")

    #slow down request rate
    time.sleep(2)



