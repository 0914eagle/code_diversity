
def get_min_cost(n, x, c):
    # Initialize variables
    min_cost = 0
    byteland_cities = []
    berland_cities = []
    disputed_cities = []
    
    # Separate the cities into three lists based on their type
    for i in range(n):
        if c[i] == "B":
            byteland_cities.append(x[i])
        elif c[i] == "R":
            berland_cities.append(x[i])
        else:
            disputed_cities.append(x[i])
    
    # Connect the cities of Byteland and the disputed cities
    for i in range(len(byteland_cities)):
        for j in range(i+1, len(byteland_cities)):
            min_cost += abs(byteland_cities[i] - byteland_cities[j])
    
    # Connect the cities of Berland and the disputed cities
    for i in range(len(berland_cities)):
        for j in range(i+1, len(berland_cities)):
            min_cost += abs(berland_cities[i] - berland_cities[j])
    
    return min_cost

def main():
    n = int(input())
    x = list(map(int, input().split()))
    c = list(input().split())
    print(get_min_cost(n, x, c))

if __name__ == '__main__':
    main()

