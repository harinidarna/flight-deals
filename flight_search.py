import requests
from pprint import pprint
from flight_data import FlightData


FLIGHT_API = "YOUR TEQUILA KIWI API"
API_KEY = "YOUR TEQUILA API KEY"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_codes(self, city_name):
        headers = {
            "apikey": API_KEY,
        }
        params = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{FLIGHT_API}/locations/query", headers=headers, params=params)
        response.raise_for_status()
        search_data = response.json()["locations"]
        return search_data[0]["code"]

    def cheap_flights(self, origin_country, iata_code, from_date, to_date):
        headers = {
            "apikey": API_KEY,
        }
        params = {
            "fly_from": origin_country,
            "fly_to": iata_code,
            "date_from": from_date,
            "date_to": to_date,
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "sort": "price",
        }
        response = requests.get(url=f"{FLIGHT_API}/v2/search", headers=headers, params=params)
        response.raise_for_status()
        details = response.json()
        data = details["data"][0]

        try:
            data
        except IndexError:
            print(f"No flights found for {iata_code}.")
            return None

        flight_data = FlightData(
            data["price"],
            data["cityFrom"],
            data["flyFrom"],
            data["cityTo"],
            data['flyTo'],
            data["route"][0]["local_departure"].split("T")[0],
            data["route"][1]["local_departure"].split("T")[0]
        )
        pprint(details)
        print(f"{data['cityTo']}: £{data['price']}")
        return flight_data
