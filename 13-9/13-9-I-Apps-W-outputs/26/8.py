
def get_min_flats(pokemons):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats visited
    min_flats = 0
    # Iterate through the Pokemons in the house
    for pokemon in pokemons:
        # If the Pokemon has not been visited yet, visit it and add its type to the set of visited types
        if pokemon not in visited_types:
            visited_types.add(pokemon)
            min_flats += 1
    # Return the minimum number of flats visited
    return min_flats

def main():
    # Read the number of flats and the types of Pokemons from stdin
    n = int(input())
    pokemons = input()
    # Call the get_min_flats function and print the result
    print(get_min_flats(pokemons))

if __name__ == '__main__':
    main()

