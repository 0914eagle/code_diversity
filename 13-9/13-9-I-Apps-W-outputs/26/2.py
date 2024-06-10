
def get_min_visits(flat_types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of visits
    min_visits = 0
    # Iterate through the flats and their types
    for flat, type in enumerate(flat_types, start=1):
        # If the type has not been visited yet, visit it and add it to the set of visited types
        if type not in visited_types:
            visited_types.add(type)
            min_visits += 1
    # Return the minimum number of visits
    return min_visits

def main():
    # Read the number of flats and their types from stdin
    n = int(input())
    flat_types = input()
    # Call the get_min_visits function and print the result
    print(get_min_visits(flat_types))

if __name__ == '__main__':
    main()

