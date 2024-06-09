
def get_cables(cities, byteland_cities, berland_cities):
    cables = []
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            if (cities[i] in byteland_cities and cities[j] in byteland_cities) or (cities[i] in berland_cities and cities[j] in berland_cities):
                cables.append((cities[i], cities[j]))
    return cables

def get_total_length(cables):
    total_length = 0
    for cable in cables:
        total_length += abs(cable[0] - cable[1])
    return total_length

def get_min_total_length(cities, byteland_cities, berland_cities):
    min_total_length = float('inf')
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            current_cables = get_cables(cities, byteland_cities, berland_cities)
            current_total_length = get_total_length(current_cables)
            if current_total_length < min_total_length:
                min_total_length = current_total_length
    return min_total_length

def main():
    n = int(input())
    cities = []
    byteland_cities = []
    berland_cities = []
    for i in range(n):
        city = int(input())
        type = input()
        cities.append(city)
        if type == 'B':
            byteland_cities.append(city)
        elif type == 'R':
            berland_cities.append(city)
    min_total_length = get_min_total_length(cities, byteland_cities, berland_cities)
    print(min_total_length)

if __name__ == '__main__':
    main()

