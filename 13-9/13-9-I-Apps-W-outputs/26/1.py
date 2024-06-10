
def get_min_visits(types):
    # Initialize a set to store the unique types
    unique_types = set()
    # Iterate through the types list
    for type in types:
        # If the type is not in the set, add it
        if type not in unique_types:
            unique_types.add(type)
    # Return the length of the unique types set
    return len(unique_types)

def main():
    # Read the number of flats and the types from stdin
    n = int(input())
    types = list(input())
    # Call the get_min_visits function and print the result
    print(get_min_visits(types))

if __name__ == '__main__':
    main()

