
def get_min_cost(n, x, c):
    # Initialize variables
    cost = 0
    prev_city = 0
    byteland_cities = []
    berland_cities = []
    disputed_cities = []
    
    # Separate the cities into three categories
    for i in range(n):
        if c[i] == 'B':
            byteland_cities.append(x[i])
        elif c[i] == 'R':
            berland_cities.append(x[i])
        else:
            disputed_cities.append(x[i])
    
    # Connect the cities with BNET cables
    for i in range(len(byteland_cities)):
        for j in range(i+1, len(byteland_cities)):
            cost += abs(byteland_cities[i] - byteland_cities[j])
    
    for i in range(len(berland_cities)):
        for j in range(i+1, len(berland_cities)):
            cost += abs(berland_cities[i] - berland_cities[j])
    
    for i in range(len(disputed_cities)):
        for j in range(i+1, len(disputed_cities)):
            cost += abs(disputed_cities[i] - disputed_cities[j])
    
    return cost

def main():
    n = int(input())
    x = list(map(int, input().split()))
    c = list(input())
    print(get_min_cost(n, x, c))

if __name__ == '__main__':
    main()

