
def get_road_companies(n, k, roads):
    # Initialize a dictionary to store the companies and the roads they own
    companies = {}
    for i in range(n):
        companies[i] = set()
    
    # Iterate over the roads and assign them to companies
    for road in roads:
        company = len(companies)
        companies[company].add(road)
    
    # Iterate over the cities and check if they have two or more roads belonging to the same company
    for city in range(n):
        for road1 in companies[city]:
            for road2 in companies[city]:
                if road1 != road2 and road1 in companies[city] and road2 in companies[city]:
                    companies[city].remove(road1)
                    companies[city].remove(road2)
    
    # Return the required number of companies and the assignment of roads to companies
    return len(companies), [companies[i].pop() for i in range(n)]

def main():
    n, k = map(int, input().split())
    roads = []
    for _ in range(n-1):
        roads.append(tuple(map(int, input().split())))
    r, c = get_road_companies(n, k, roads)
    print(r)
    print(*c)

if __name__ == '__main__':
    main()

