import requests, json

# URL to get the route ID
ROUTE_URL = 'http://svc.metrotransit.org/NexTrip/Routes?format=json'
# URL to get the direction ID
DIRECTIONS_URL = 'http://svc.metrotransit.org/NexTrip/Directions/{ROUTE_ID}?format=json'
# URL to get the stop ID
STOPS_URL = 'http://svc.metrotransit.org/NexTrip/Stops/{ROUTE_ID}/{DIR_ID}?format=json'
# Final ID to get the time til next stop
MAIN_URL = 'http://svc.metrotransit.org/NexTrip/{ROUTE_ID}/{DIR_ID}/{STOP_ID}?format=json'


def get_route_id(route):
    response_data = requests.get(ROUTE_URL).json()
    for item in response_data:
        if route in item['Description'].lower():
            return item['Route']
    return -1


def get_direction_id(direction, route_id):
    response_data = requests.get(DIRECTIONS_URL.format(ROUTE_ID=route_id)).json()
    for item in response_data:
        if direction in item['Text'].lower():
            return item['Value']
    return -1


def get_stop_id(stop, route_id, dir_id):
    response_data = requests.get(STOPS_URL.format(ROUTE_ID=route_id, DIR_ID=dir_id)).json()
    for item in response_data:
        if stop in item['Text'].lower():
            return item['Value']
    return -1


def get_time_to_next_bus(route_id, dir_id, stop_id):
    response = requests.get(MAIN_URL.format(ROUTE_ID=route_id, DIR_ID=dir_id, STOP_ID=stop_id)).json()
    return response[0]['DepartureText']