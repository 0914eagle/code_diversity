
def get_cables(n, cities):
    
    # Initialize variables
    total_length = 0
    byteland_cities = []
    berland_cities = []
    disputed_cities = []

    # Sort cities by coordinate
    cities.sort(key=lambda x: x[0])

    # Separate cities into Byteland, Berland, and disputed cities
    for city in cities:
        if city[1] == "B":
            byteland_cities.append(city)
        elif city[1] == "R":
            berland_cities.append(city)
        else:
            disputed_cities.append(city)

    # Connect Byteland cities
    for i in range(len(byteland_cities) - 1):
        total_length += abs(byteland_cities[i + 1][0] - byteland_cities[i][0])

    # Connect Berland cities
    for i in range(len(berland_cities) - 1):
        total_length += abs(berland_cities[i + 1][0] - berland_cities[i][0])

    # Connect disputed cities
    for city in disputed_cities:
        if city[0] < byteland_cities[0][0]:
            total_length += abs(byteland_cities[0][0] - city[0])
        elif city[0] > byteland_cities[-1][0]:
            total_length += abs(byteland_cities[-1][0] - city[0])
        elif city[0] < berland_cities[0][0]:
            total_length += abs(berland_cities[0][0] - city[0])
        elif city[0] > berland_cities[-1][0]:
            total_length += abs(berland_cities[-1][0] - city[0])

    return total_length

def main():
    n = int(input())
    cities = []
    for i in range(n):
        x, c = input().split()
        cities.append((int(x), c))
    print(get_cables(n, cities))

if __name__ == "__main__":
    main()

