
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
            num_bad_cities = 0
            for city in city_to_companies:
                if city in bad_cities and company in city_to_companies[city]:
                    num_bad_cities += 1
            if num_bad_cities > max_company:
                max_company = num_bad_cities
        
        # Merge the company with the most roads entering bad cities with the next company
        company_to_merge = 0
        for company in range(1, num_companies + 1):
            if company not in bad_cities and company != max_company:
                company_to_merge = company
                break
        merge_companies(company_to_merge, max_company, city_to_companies)
        num_companies -= 1
        
        # Update the set of bad cities
        bad_cities = set()
        for city, companies in city_to_companies.items():
            if len(companies) > 1:
                bad_cities.add(city)
    
    return num_companies

def merge_companies(company_to_merge, company_to_merge_with, city_to_companies):
    for city, companies in city_to_companies.items():
        if company_to_merge in companies:
            companies.remove(company_to_merge)
            companies.add(company_to_merge_with)


