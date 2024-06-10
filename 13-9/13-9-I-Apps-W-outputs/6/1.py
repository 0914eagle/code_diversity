
def get_cable_length(city_1, city_2):
    return abs(city_1 - city_2)

def get_min_cables(cities, type_1, type_2):
    min_cables = []
    for i in range(len(cities)):
        if cities[i] == type_1:
            for j in range(i+1, len(cities)):
                if cities[j] == type_2:
                    min_cables.append(get_cable_length(cities[i], cities[j]))
    return min_cables

def get_total_length(min_cables):
    total_length = 0
    for cable in min_cables:
        total_length += cable
    return total_length

def main():
    n = int(input())
    cities = []
    for i in range(n):
        city = int(input())
        type = input()
        cities.append((city, type))
    
    byteland_cables = get_min_cables(cities, 'B', 'P')
    berland_cables = get_min_cables(cities, 'R', 'P')
    
    total_length = get_total_length(byteland_cables + berland_cables)
    print(total_length)

if __name__ == '__main__':
    main()

