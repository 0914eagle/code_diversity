
def solve(n, k, roads):
    # Initialize the company assignments
    companies = [[] for _ in range(n)]
    for road in roads:
        companies[road[0]].append(road[1])
        companies[road[1]].append(road[0])

    # Find the number of companies that have two or more roads entering a city
    num_companies_per_city = [0] * n
    for company in companies:
        for city in company:
            num_companies_per_city[city] += 1

    # Find the minimum number of companies needed to have at most k cities with two or more roads
    min_companies = 1
    while min_companies <= n - 1:
        num_cities_with_two_or_more_roads = 0
        for city, num_companies in enumerate(num_companies_per_city):
            if num_companies >= min_companies:
                num_cities_with_two_or_more_roads += 1
        if num_cities_with_two_or_more_roads <= k:
            break
        min_companies += 1

    # Assign the companies to the roads
    company_assignments = [0] * n
    for road in roads:
        company_assignments[road[0]] = min_companies
        company_assignments[road[1]] = min_companies

    return min_companies, company_assignments

