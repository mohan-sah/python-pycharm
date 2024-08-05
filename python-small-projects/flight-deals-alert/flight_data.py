class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(self, data):
        """
        Parses flight data from Amadeus Api to identify cheapest one

        Args: json data with flight args

        Returns: instance of Flightdata class representing the cheapest flight found,
        or 'NA' to all fields if non found

        It iterates through a list of data and updates only the cheapest option .
        """

        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])

        origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        # starting line set
        cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date)

        # now let's start comparing all prices one by one
        for flight in data['data']:
            price = float(flight['price']['grandTotal'])
            if cheapest_flight.price != "N/A" and price < lowest_price:
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination_airport, out_date, return_date)
                print(f"lowest price to {destination_airport} is rs.{lowest_price}")

        return cheapest_flight
