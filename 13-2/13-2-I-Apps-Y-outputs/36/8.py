
def solve(n, k, roads):
    # Initialize the number of companies to be the number of roads
    num_companies = len(roads)
    # Initialize a dictionary to map each city to the companies that own roads entering it
    city_to_companies = {}
    for road in roads:
        city1, city2 = road
        if city1 not in city_to_companies:
            city_to_companies[city1] = set()
        if city2 not in city_to_companies:
            city_to_companies[city2] = set()
        city_to_companies[city1].add(num_companies)
        city_to_companies[city2].add(num_companies)
        num_companies += 1
    
    # Initialize a set to store the cities that have two or more roads belonging to the same company
    bad_cities = set()
    for city, companies in city_to_companies.items():
        if len(companies) > 1:
            bad_cities.add(city)
    
    # If the number of bad cities is less than or equal to k, we can stop here
    if len(bad_cities) <= k:
        return num_companies - 1
    
    # Otherwise, we need to merge companies to reduce the number of bad cities
    while len(bad_cities) > k:
        # Find the company with the most roads entering bad cities
        max_company = 0
        for company in range(1, num_companies + 1):
            num_bad_roads = 0
            for road in roads:
                city1, city2 = road
                if city1 in bad_cities or city2 in bad_cities:
                    num_bad_roads += 1
            if num_bad_roads > max_company:
                max_company = num_bad_roads
        
        # Merge the company with the most roads entering bad cities with the next company
        num_companies -= 1
        for road in roads:
            city1, city2 = road
            if city1 in bad_cities or city2 in bad_cities:
                city_to_companies[city1].remove(max_company)
                city_to_companies[city1].add(num_companies + 1)
                city_to_companies[city2].remove(max_company)
                city_to_companies[city2].add(num_companies + 1)
    
    # Return the number of companies and the mapping of roads to companies
    return num_companies, [city_to_companies[road[0]].pop() for road in roads]

