
def find_minimal_number_of_companies(n, k, roads):
    # Initialize a dictionary to keep track of the companies and the cities they serve
    companies = {}
    for road in roads:
        # If the company is already in the dictionary, add the city to the list of cities served by the company
        if road[0] in companies:
            companies[road[0]].append(road[1])
        # Otherwise, create a new key in the dictionary with the city as the value
        else:
            companies[road[0]] = [road[1]]
    
    # Initialize a set to keep track of the cities with multiple roads
    multiple_cities = set()
    for company, cities in companies.items():
        # If the company serves more than one city, add those cities to the set
        if len(cities) > 1:
            multiple_cities.update(cities)
    
    # Return the number of companies needed to assign each road to a company
    return len(multiple_cities) + 1

def assign_companies(n, k, roads):
    # Find the minimal number of companies needed to assign each road to a company
    num_companies = find_minimal_number_of_companies(n, k, roads)
    
    # Initialize a dictionary to keep track of the companies and the cities they serve
    companies = {}
    for i in range(num_companies):
        companies[i+1] = []
    
    # Assign each road to a company
    for road in roads:
        # If the company is already in the dictionary, add the city to the list of cities served by the company
        if road[0] in companies:
            companies[road[0]].append(road[1])
        # Otherwise, create a new key in the dictionary with the city as the value
        else:
            companies[road[0]] = [road[1]]
    
    # Return the list of companies and the cities they serve
    return [companies[i+1] for i in range(num_companies)]

if __name__ == '__main__':
    n, k = map(int, input().split())
    roads = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        roads.append([x, y])
    print(assign_companies(n, k, roads))

