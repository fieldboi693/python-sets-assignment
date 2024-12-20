# Flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to (intersection)
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# 2. Destinations unique to your airline (difference)
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# 3. Destinations neither airline flies to
# Assuming a hypothetical universal set of destinations
universal_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "NRT"}
destinations_neither_airline_flies_to = universal_destinations.difference(our_routes.union(competitor_routes))
print("Destinations neither airline flies to:", destinations_neither_airline_flies_to)

# Given list of customer IDs
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
unique_customer_ids = set(customer_ids)

# Display the set of unique customer IDs
print("Unique customer IDs:", unique_customer_ids)