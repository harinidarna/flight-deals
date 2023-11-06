import requests

SHEETY_ENDPOINT = "https://api.sheety.co/eca8fdcd4956d234bb44267b75104809/copyOfFlightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet = requests.get(url=SHEETY_ENDPOINT)
        self.sheet.raise_for_status()
        self.prices = self.sheet.json()

    def put_codes(self, sheet_data):
        cities_list = sheet_data["prices"]
        for city in cities_list:
            row_id = city["id"]
            row_code = city["iataCode"]
            sheety_rows = f"{SHEETY_ENDPOINT}/{row_id}"
            row_update = {
                "price": {
                    "iataCode": row_code
                }
            }
            response = requests.put(url=sheety_rows, json=row_update)
            response.raise_for_status()
