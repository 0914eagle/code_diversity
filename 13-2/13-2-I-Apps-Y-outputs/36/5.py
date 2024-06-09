
def solve(n, k, roads):
    # Initialize the company assignments
    companies = [[] for _ in range(n)]
    for road in roads:
        companies[road[0]].append(road[1])
        companies[road[1]].append(road[0])

    # Find the companies with the most roads
    max_roads = max([len(company) for company in companies])
    companies_with_max_roads = [i for i, company in enumerate(companies) if len(company) == max_roads]

    # If the number of companies with the most roads is less than or equal to k, return the number of companies
    if len(companies_with_max_roads) <= k:
        return len(companies_with_max_roads)

    # Otherwise, find the company with the least number of roads
    min_roads = min([len(company) for company in companies])
    companies_with_min_roads = [i for i, company in enumerate(companies) if len(company) == min_roads]

    # Return the number of companies with the least number of roads
    return len(companies_with_min_roads)

