
def get_min_visited_flats(flat_types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats visited
    min_visited_flats = 0
    # Iterate through the flats and their types
    for flat, type in enumerate(flat_types):
        # If the type has not been visited yet, visit it and add it to the set of visited types
        if type not in visited_types:
            visited_types.add(type)
            min_visited_flats += 1
    # Return the minimum number of flats visited
    return min_visited_flats

def main():
    n = int(input())
    flat_types = input()
    print(get_min_visited_flats(flat_types))

if __name__ == '__main__':
    main()

