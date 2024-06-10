
def get_min_visited_flats(types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats visited
    min_visited_flats = 0
    # Iterate through the types of Pokemons
    for type in types:
        # If the type has not been visited yet, visit it and add it to the set of visited types
        if type not in visited_types:
            visited_types.add(type)
            min_visited_flats += 1
    # Return the minimum number of flats visited
    return min_visited_flats

def main():
    # Read the number of flats and the types of Pokemons from stdin
    n = int(input())
    types = input()
    # Call the get_min_visited_flats function and print the result
    print(get_min_visited_flats(types))

if __name__ == '__main__':
    main()

