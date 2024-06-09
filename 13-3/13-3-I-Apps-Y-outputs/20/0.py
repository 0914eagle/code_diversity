
def solve(n, m, prefectures):
    # Initialize a list to store the ID numbers for all the cities
    id_numbers = []
    
    # Iterate over the prefectures and their cities
    for prefecture, cities in enumerate(prefectures, start=1):
        # Sort the cities by their establishment year
        sorted_cities = sorted(cities, key=lambda x: x[1])
        
        # Iterate over the sorted cities and assign ID numbers to them
        for i, (city, year) in enumerate(sorted_cities, start=1):
            # Format the ID number as a string with six digits for the prefecture and six digits for the city index
            id_number = f"{prefecture:06d}{i:06d}"
            id_numbers.append(id_number)
    
    # Return the list of ID numbers for all the cities
    return id_numbers

