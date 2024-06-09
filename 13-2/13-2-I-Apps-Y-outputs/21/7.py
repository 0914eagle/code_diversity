
def solve(trips, queries):
    # Create a dictionary to store the trips
    trips_dict = {}
    for trip in trips:
        country, year = trip
        if country not in trips_dict:
            trips_dict[country] = []
        trips_dict[country].append(year)

    # Iterate over the queries and return the corresponding year
    for query in queries:
        country, k = query
        year = trips_dict[country][k-1]
        print(year)

# Test the function with example input
trips = [
    ("Iceland", 2016),
    ("Sweden", 2015),
    ("Iceland", 1982),
    ("Norway", 1999)
]
queries = [
    ("Sweden", 1),
    ("Iceland", 1),
    ("Iceland", 2)
]
solve(trips, queries)

