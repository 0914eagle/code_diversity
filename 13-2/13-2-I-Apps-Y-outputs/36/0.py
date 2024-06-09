
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
    
    # Otherwise, we need to merge some companies to reduce the number of bad cities
    while len(bad_cities) > k:
        # Find the company with the most roads entering bad cities
        max_company = 0
        for company, cities in city_to_companies.items():
            if len(cities & bad_cities) > 0 and len(cities) > max_company:
                max_company = len(cities)
        
        # Merge the company with the most roads entering bad cities with the company next to it
        merged_company = max_company + 1
        for city in city_to_companies:
            if city_to_companies[city] == {max_company}:
                city_to_companies[city].add(merged_company)
                city_to_companies[city].remove(max_company)
        
        # Update the set of bad cities
        bad_cities = set()
        for city, companies in city_to_companies.items():
            if len(companies) > 1:
                bad_cities.add(city)
    
    return num_companies - 1

