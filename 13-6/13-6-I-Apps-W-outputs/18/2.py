
def get_criminal_information(city_index, num_cities, criminals):
    # Initialize a dictionary to store the information about the criminals
    criminal_info = {}

    # Iterate over the criminals and store the information in the dictionary
    for criminal in criminals:
        distance = abs(city_index - criminal)
        if distance in criminal_info:
            criminal_info[distance] += 1
        else:
            criminal_info[distance] = 1

    return criminal_info

def catch_criminals(city_index, num_cities, criminals, criminal_info):
    # Initialize a set to store the indices of the cities where criminals are caught
    caught_cities = set()

    # Iterate over the information about the criminals and catch the criminals in the cities where they are sure to be
    for distance, num_criminals in criminal_info.items():
        for i in range(distance):
            city = (city_index - i) % num_cities
            if city not in caught_cities and criminals[city] == 1:
                caught_cities.add(city)
                num_criminals -= 1
        if num_criminals == 0:
            break

    return len(caught_cities)

def main():
    city_index, num_cities = map(int, input().split())
    criminals = list(map(int, input().split()))
    criminal_info = get_criminal_information(city_index, num_cities, criminals)
    print(catch_criminals(city_index, num_cities, criminals, criminal_info))

if __name__ == '__main__':
    main()

