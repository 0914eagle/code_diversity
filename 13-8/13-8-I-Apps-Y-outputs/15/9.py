
def get_min_companies(n, k, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

    # Initialize a list to store the companies and the number of cities each company can own
    companies = [(i, 0) for i in range(1, n)]

    # Function to assign companies to roads
    def assign_companies(graph, companies):
        # Base case: if all cities are assigned to companies, return the list of companies
        if all(company[1] > 0 for company in companies):
            return companies

        # Initialize a list to store the cities that are not assigned to any company
        unassigned_cities = []

        # Iterate over the cities in the graph
        for city in range(n):
            # If the city is not assigned to any company, add it to the list of unassigned cities
            if all(company[0] != city for company in companies):
                unassigned_cities.append(city)

        # If there are no unassigned cities, return the list of companies
        if not unassigned_cities:
            return companies

        # Iterate over the companies
        for company in companies:
            # If the company has not reached its limit, try to assign it to an unassigned city
            if company[1] < k:
                for city in unassigned_cities:
                    # If the company can own the city, assign it to the company and remove the city from the list of unassigned cities
                    if can_own_city(graph, company, city):
                        company[1] += 1
                        unassigned_cities.remove(city)
                        break

        # If there are no more unassigned cities, return the list of companies
        if not unassigned_cities:
            return companies

        # Recursively call the function to assign companies to the remaining unassigned cities
        return assign_companies(graph, companies)

    # Function to check if a company can own a city
    def can_own_city(graph, company, city):
        # If the company has already owned k cities, it cannot own any more cities
        if company[1] == k:
            return False

        # If the city is already owned by another company, the company cannot own it
        if any(company[0] != i for i, _ in companies):
            return False

        # If the city is not connected to any other city owned by the company, the company cannot own it
        if not any(city in graph[i] for i in range(n) if companies[i][0] == company[0]):
            return False

        return True

    # Call the function to assign companies to roads
    companies = assign_companies(graph, companies)

    # Return the list of companies and the number of cities each company can own
    return [(company[0], company[1]) for company in companies]

def main():
    n, k = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(n - 1)]
    companies = get_min_companies(n, k, roads)
    print(len(companies))
    for company in companies:
        print(company[0], end=" ")

if __name__ == '__main__':
    main()

