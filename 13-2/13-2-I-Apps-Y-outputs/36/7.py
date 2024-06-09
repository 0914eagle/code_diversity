
def solve(n, k, roads):
    # Initialize the company assignments
    companies = [[] for _ in range(n)]
    for road in roads:
        companies[road[0]].append(road[1])
        companies[road[1]].append(road[0])

    # Find the number of companies that have two or more roads entering the city
    num_companies_per_city = [0] * n
    for company in companies:
        for city in company:
            num_companies_per_city[city] += 1

    # Find the minimum number of companies needed to assign each road to a company
    min_companies = 0
    for num_companies in num_companies_per_city:
        if num_companies > k:
            min_companies += 1

    # Return the minimum number of companies needed and the company assignments
    return min_companies, companies

