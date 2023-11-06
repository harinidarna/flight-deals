class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, city_from, fly_from, city_to, fly_to, outbound_date, inbound_date):
        self.price = price
        self.departure_city_name = city_from
        self.departure_iata_code = fly_from
        self.arrival_city_name = city_to
        self.arrival_airport_iata_code = fly_to
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
