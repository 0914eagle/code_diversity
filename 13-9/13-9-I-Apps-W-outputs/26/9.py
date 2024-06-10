
def get_min_visits(n, types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of visits
    min_visits = 0
    # Iterate through the types of Pokemons
    for type in types:
        # If the type has not been visited yet, visit it and increment the minimum number of visits
        if type not in visited_types:
            visited_types.add(type)
            min_visits += 1
    # Return the minimum number of visits
    return min_visits

def main():
    # Read the number of flats and the types of Pokemons from stdin
    n = int(input())
    types = input()
    # Call the get_min_visits function and print the result
    print(get_min_visits(n, types))

if __name__ == '__main__':
    main()

