
def solve(trips, queries):
    trips_dict = {}
    for trip in trips:
        country, year = trip
        if country not in trips_dict:
            trips_dict[country] = []
        trips_dict[country].append(year)

    result = []
    for query in queries:
        country, k = query
        result.append(trips_dict[country][k-1])

    return result

