
def get_companies(n, k, roads):
    # Initialize a dictionary to store the companies and the cities they own
    companies = {}
    for i in range(1, n+1):
        companies[i] = set()
    
    # Iterate over the roads and assign them to companies
    for road in roads:
        company = len(companies) + 1
        companies[company].add(road[0])
        companies[company].add(road[1])
    
    # Check if the number of cities with two or more roads belonging to one company is at most k
    not_good_cities = 0
    for city in range(1, n+1):
        if len(companies[city]) > 1:
            not_good_cities += 1
    
    # If the number of not good cities is greater than k, return -1
    if not_good_cities > k:
        return -1
    
    # Otherwise, return the number of companies and the company assignments
    return len(companies), [companies[i] for i in range(1, len(companies)+1)]

def main():
    n, k = map(int, input().split())
    roads = []
    for _ in range(n-1):
        roads.append(list(map(int, input().split())))
    print(get_companies(n, k, roads))

if __name__ == '__main__':
    main()

