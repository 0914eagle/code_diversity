
def get_cables_cost(cities, byteland_cities, berland_cities):
    
    cost = 0
    for i in range(len(cities) - 1):
        for j in range(i + 1, len(cities)):
            if (cities[i] in byteland_cities and cities[j] in byteland_cities) or (cities[i] in berland_cities and cities[j] in berland_cities):
                cost += abs(cities[i] - cities[j])
    return cost

def get_min_cables_cost(cities, byteland_cities, berland_cities):
    
    min_cost = float("inf")
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            if (cities[i] in byteland_cities and cities[j] in byteland_cities) or (cities[i] in berland_cities and cities[j] in berland_cities):
                cost = get_cables_cost(cities, byteland_cities, berland_cities)
                if cost < min_cost:
                    min_cost = cost
    return min_cost

def main():
    n = int(input())
    cities = []
    byteland_cities = []
    berland_cities = []
    for i in range(n):
        x, c = map(int, input().split())
        cities.append(x)
        if c == "B":
            byteland_cities.append(x)
        elif c == "R":
            berland_cities.append(x)
    print(get_min_cables_cost(cities, byteland_cities, berland_cities))

if __name__ == '__main__':
    main()

