
def get_minimal_number_of_companies(n, k, roads):
    # Initialize a dictionary to map each city to the companies that own a road entering it
    city_to_companies = {}
    for road in roads:
        city1, city2 = road
        if city1 not in city_to_companies:
            city_to_companies[city1] = set()
        if city2 not in city_to_companies:
            city_to_companies[city2] = set()
        city_to_companies[city1].add(road[2])
        city_to_companies[city2].add(road[2])
    
    # Initialize a set to store the cities that have two or more roads belonging to the same company
    bad_cities = set()
    for city, companies in city_to_companies.items():
        if len(companies) > 1:
            bad_cities.add(city)
    
    # If the number of bad cities is less than or equal to k, return the number of companies as the answer
    if len(bad_cities) <= k:
        return len(set(city_to_companies.values()))
    
    # Otherwise, recursively try all possible combinations of companies and find the minimum number of companies that can assign each road to a company in such a way that the number of bad cities doesn't exceed k
    min_companies = n
    for companies in combinations(range(1, len(city_to_companies) + 1), len(city_to_companies)):
        company_to_cities = {}
        for city, company in zip(city_to_companies, companies):
            if company not in company_to_cities:
                company_to_cities[company] = set()
            company_to_cities[company].add(city)
        bad_cities = set()
        for company, cities in company_to_cities.items():
            if len(cities) > 1:
                bad_cities.update(cities)
        if len(bad_cities) <= k and len(company_to_cities) < min_companies:
            min_companies = len(company_to_cities)
    
    return min_companies

def main():
    n, k = map(int, input().split())
    roads = []
    for _ in range(n - 1):
        roads.append(list(map(int, input().split())))
    print(get_minimal_number_of_companies(n, k, roads))

if __name__ == '__main__':
    main()

