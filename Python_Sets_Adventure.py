# Define the flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to (intersection)
common_destinations = our_routes & competitor_routes
print("Destinations both airlines fly to:", common_destinations)

# 2. Destinations unique to your airline (difference)
unique_to_our_airline = our_routes - competitor_routes
print("Destinations unique to our airline:", unique_to_our_airline)

# 3. Check if there are destinations neither airline flies to (universe set approach)
# Assuming a hypothetical universal set of destinations
universal_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "NRT"}
destinations_neither_airline_flies_to = universal_destinations - (our_routes | competitor_routes)
print("Destinations neither airline flies to:", destinations_neither_airline_flies_to)