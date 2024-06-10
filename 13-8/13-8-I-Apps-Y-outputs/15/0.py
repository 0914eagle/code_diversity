
def get_min_number_of_companies(n, k, edges):
    # Initialize a dictionary to store the companies and the cities they own
    companies = {}
    for i in range(n):
        companies[i+1] = set()
    
    # Iterate over the edges and assign them to companies
    for edge in edges:
        # If the edge is not already owned by a company, assign it to a new company
        if edge not in companies:
            companies[len(companies)+1] = set([edge])
        # If the edge is already owned by a company, add it to that company
        else:
            companies[edge].add(edge)
    
    # Initialize a set to store the cities with two or more roads belonging to the same company
    bad_cities = set()
    
    # Iterate over the companies and check if they own two or more roads entering the same city
    for company, roads in companies.items():
        for road in roads:
            # If the company owns two or more roads entering the same city, add that city to the bad_cities set
            if len(roads) > 1:
                bad_cities.add(road[0])
    
    # Return the minimum number of companies needed to have at most k bad cities
    return len(companies), len(bad_cities) <= k

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n-1):
        x, y = map(int, input().split())
        edges.append((x, y))
    
    r, is_feasible = get_min_number_of_companies(n, k, edges)
    if is_feasible:
        print(r)
        for i in range(n-1):
            print(i+1, end=" ")
        print()
    else:
        print(-1)

if __name__ == '__main__':
    main()

