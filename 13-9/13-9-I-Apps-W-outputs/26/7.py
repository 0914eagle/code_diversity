
def get_min_flats_to_visit(types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats to visit
    min_flats = 0
    # Loop through the types of Pokemons in the house
    for type in types:
        # If the type has not been visited yet, visit it and increment the minimum number of flats to visit
        if type not in visited_types:
            visited_types.add(type)
            min_flats += 1
    # Return the minimum number of flats to visit
    return min_flats

def main():
    # Read the number of flats in the house and the types of Pokemons from the input
    n = int(input())
    types = input()
    # Call the get_min_flats_to_visit function and store the result in a variable
    min_flats = get_min_flats_to_visit(types)
    # Print the minimum number of flats to visit
    print(min_flats)

if __name__ == '__main__':
    main()

