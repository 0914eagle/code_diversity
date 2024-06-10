
def get_min_flats(n, types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats visited
    min_flats = 0
    # Initialize a variable to store the current flat number
    current_flat = 1
    # Loop through each type in the input row
    for type in types:
        # If the current type has not been visited yet, visit it and add it to the set of visited types
        if type not in visited_types:
            visited_types.add(type)
            min_flats += 1
        # If all types have been visited, break the loop
        if len(visited_types) == n:
            break
        # Move to the next flat in the row
        current_flat += 1
    return min_flats

def main():
    n = int(input())
    types = input()
    print(get_min_flats(n, types))

if __name__ == '__main__':
    main()

