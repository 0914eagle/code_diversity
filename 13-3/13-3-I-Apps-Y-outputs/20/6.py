
def solve(N, M, prefectures):
    # Sort the prefectures by their establishment year
    sorted_prefectures = sorted(prefectures, key=lambda x: x[1])

    # Create a dictionary to map each prefecture to its cities
    prefecture_to_cities = {}
    for prefecture in sorted_prefectures:
        prefecture_id, establishment_year = prefecture
        if prefecture_id not in prefecture_to_cities:
            prefecture_to_cities[prefecture_id] = []
        prefecture_to_cities[prefecture_id].append(establishment_year)

    # Create a list to store the ID numbers for all the cities
    city_ids = []

    # Iterate over the prefectures and their cities
    for prefecture_id, cities in prefecture_to_cities.items():
        # Sort the cities by their establishment year
        sorted_cities = sorted(cities)

        # Iterate over the cities and assign an ID number to each one
        for i, city in enumerate(sorted_cities):
            # Format the ID number as a string with six digits for the prefecture ID and six digits for the city index
            id_number = f"{prefecture_id:06d}{i:06d}"
            city_ids.append(id_number)

    # Return the list of ID numbers for all the cities
    return city_ids

