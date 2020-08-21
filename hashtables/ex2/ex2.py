#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Set a dictionary for the flights
    flight = {}

    # Set a list for the routes
    route = []

    # Loop through the parameter length (amount of tickets/stops)
    for i in range(length):
        # Set the key as the current ticket's source
        key = tickets[i].source
        # Set the value as the current ticket's destination
        value = tickets[i].destination

        # Put the current stop in the flight dict with it's new key/value
        flight[key] = value

    """
    If the key is "NONE", it's the beginning of the route
    If the key's value is "NONE", it's the final destination
    Add to the route list until the value of key is "NONE"
    """

    # Set the beginning of the route
    key = flight["NONE"]

    # Start the route-adding loop
    while key != "NONE":
        # Append the current key to the route
        route.append(key)

        # Set the key to the next destination
        key = flight[key]
    
    # Append the final key to the route
    # This will always have a value of "NONE"
    route.append(key)

    # Return the list of routes in their correct order
    return route
