
def get_companies(n, k, roads):
    # Initialize a dictionary to map each city to the companies that own roads entering it
    city_companies = {}
    for road in roads:
        city1, city2 = road
        if city1 not in city_companies:
            city_companies[city1] = set()
        if city2 not in city_companies:
            city_companies[city2] = set()
        city_companies[city1].add(road[2])
        city_companies[city2].add(road[2])

    # Initialize a set to store the companies that own at least two roads entering a city
    bad_companies = set()
    for city, companies in city_companies.items():
        if len(companies) > 1:
            bad_companies |= companies

    # Return the minimum number of companies needed to avoid having more than k bad companies
    return min(n - 1, k + 1, len(bad_companies) + 1)

def get_road_assignments(n, k, roads):
    # Initialize a dictionary to map each road to a company
    road_company = {}
    for road in roads:
        road_company[road] = 1

    # Initialize a set to store the companies that own at least two roads entering a city
    bad_companies = set()
    for road in roads:
        city1, city2 = road
        if city1 not in city_companies:
            city_companies[city1] = set()
        if city2 not in city_companies:
            city_companies[city2] = set()
        city_companies[city1].add(road[2])
        city_companies[city2].add(road[2])

    # Return the minimum number of companies needed to avoid having more than k bad companies
    return min(n - 1, k + 1, len(bad_companies) + 1)

def main():
    n, k = map(int, input().split())
    roads = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    print(get_companies(n, k, roads))
    print(*get_road_assignments(n, k, roads))

if __name__ == '__main__':
    main()

