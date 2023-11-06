# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data = DataManager()
search = FlightSearch()
notify = NotificationManager()
now = datetime.now()

sheet_data = data.prices
tomorrow = now + timedelta(days=1)
next_six_months = now + timedelta(days=180)

#  poulate the IATA codes in google sheet
if sheet_data["prices"][0]["iataCode"] == "":
    for index in sheet_data["prices"]:
        city_name = index["city"]
        iata_code = search.get_iata_codes(city_name)
        index["iataCode"] = iata_code
    data.put_codes(sheet_data)

# get flight details for every city
for index in sheet_data["prices"]:
    flight = search.cheap_flights(
        ORIGIN_CITY_IATA,
        index["iataCode"],
        tomorrow.strftime("%d/%m/%Y"),
        next_six_months.strftime("%d/%m/%Y"),
    )
    if flight.price < index["lowestPrice"]:
        message = (f"Lowest Price Alert! Only £{flight.price} to fly from {flight.departure_city_name}-"
                   f"{flight.departure_iata_code} to {flight.arrival_city_name}-{flight.arrival_airport_iata_code}, "
                   f"from {flight.outbound_date} to {flight.inbound_date}.")
        notify.send_message(message=message)
pprint(sheet_data)
