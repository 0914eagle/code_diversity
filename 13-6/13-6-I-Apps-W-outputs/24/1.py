
def get_min_cost(n, x, c):
    # Initialize variables
    min_cost = 0
    prev_city = 0
    curr_city = 0
    next_city = 1
    city_types = []
    city_coords = []
    
    # Iterate through the input and create a list of city types and coordinates
    for i in range(n):
        city_types.append(c[i])
        city_coords.append(x[i])
    
    # Iterate through the list of city types and coordinates and calculate the minimum cost
    while next_city < n:
        if city_types[next_city] == city_types[prev_city]:
            min_cost += city_coords[next_city] - city_coords[prev_city]
        prev_city = curr_city
        curr_city = next_city
        next_city += 1
    
    return min_cost

def main():
    n = int(input())
    x = list(map(int, input().split()))
    c = list(input())
    print(get_min_cost(n, x, c))

if __name__ == '__main__':
    main()

