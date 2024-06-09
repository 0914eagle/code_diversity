
def get_cable_cost(city1, city2):
    return abs(city1 - city2)

def connect_cities(cities, type1, type2):
    cities_to_connect = []
    for i in range(len(cities)):
        if cities[i][1] == type1 or cities[i][1] == type2:
            cities_to_connect.append(cities[i])
    
    total_cost = 0
    for i in range(len(cities_to_connect)):
        for j in range(i+1, len(cities_to_connect)):
            total_cost += get_cable_cost(cities_to_connect[i][0], cities_to_connect[j][0])
    
    return total_cost

def main():
    n = int(input())
    cities = []
    for i in range(n):
        city = input().split()
        cities.append((int(city[0]), city[1]))
    
    print(connect_cities(cities, "B", "R"))

if __name__ == '__main__':
    main()

