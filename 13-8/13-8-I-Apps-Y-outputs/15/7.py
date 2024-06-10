
def get_input():
    n, k = map(int, input().split())
    roads = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, k, roads

def solve(n, k, roads):
    # Initialize the company assignments
    company_assignments = [0] * (n-1)
    
    # Initialize the number of companies
    num_companies = 1
    
    # Loop through the roads
    for i in range(n-1):
        # If the road has not been assigned to a company, assign it to the current company
        if company_assignments[i] == 0:
            company_assignments[i] = num_companies
            num_companies += 1
        # If the road has already been assigned to a company, check if the current company is the same as the previous company
        else:
            if company_assignments[i] != num_companies:
                company_assignments[i] = num_companies
                num_companies += 1
    
    # Find the number of cities with two or more roads belonging to one company
    num_cities_with_two_or_more_roads = 0
    for i in range(n):
        num_roads_for_city = 0
        for j in range(n-1):
            if roads[j][0] == i or roads[j][1] == i:
                num_roads_for_city += 1
        if num_roads_for_city >= 2:
            num_cities_with_two_or_more_roads += 1
    
    # Return the number of companies and the company assignments if the number of cities with two or more roads belonging to one company is at most k, otherwise return -1
    if num_cities_with_two_or_more_roads <= k:
        return num_companies, company_assignments
    else:
        return -1, []

def main():
    n, k, roads = get_input()
    num_companies, company_assignments = solve(n, k, roads)
    print(num_companies)
    print(" ".join(map(str, company_assignments)))

if __name__ == '__main__':
    main()

