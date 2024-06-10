
def get_companies(n, k, roads):
    # Initialize a dictionary to map each city to the companies that own roads entering it
    city_to_companies = {i: set() for i in range(1, n + 1)}

    # Iterate over the roads and add the companies that own each road to the dictionary
    for road in roads:
        city_to_companies[road[0]].add(road[2])
        city_to_companies[road[1]].add(road[2])

    # Initialize a set to store the companies that own two or more roads entering a city
    bad_companies = set()

    # Iterate over the cities and check if any company owns two or more roads entering it
    for city, companies in city_to_companies.items():
        if len(companies) > 1:
            bad_companies.update(companies)

    # Return the minimum number of companies needed to privatize the roads while avoiding unfairness
    return len(bad_companies) + 1

def get_road_owners(n, k, roads):
    # Initialize a dictionary to map each road to a company
    road_to_company = {i: 0 for i in range(1, n + 1)}

    # Initialize a set to store the companies that own two or more roads entering a city
    bad_companies = set()

    # Iterate over the roads and assign them to companies
    for i, road in enumerate(roads, 1):
        company = i % (n - 1) + 1
        road_to_company[road[0]] = company
        road_to_company[road[1]] = company

    # Return the list of companies that own each road
    return [road_to_company[i] for i in range(1, n + 1)]

if __name__ == '__main__':
    n, k = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(n - 1)]
    r = get_companies(n, k, roads)
    print(r)
    print(*get_road_owners(n, k, roads))

