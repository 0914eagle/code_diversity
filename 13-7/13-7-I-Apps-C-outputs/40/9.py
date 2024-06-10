
def get_shortest_test_scheme(k, durations):
    # Sort the durations in descending order
    durations.sort(reverse=True)
    
    # Initialize the test scheme with the first allergen
    test_scheme = [durations[0]]
    
    # Iterate over the remaining allergens
    for i in range(1, k):
        # Check if the current allergen can be added to the test scheme without violating the non-adaptive property
        if durations[i] >= test_scheme[-1]:
            test_scheme.append(durations[i])
    
    # Return the length of the test scheme
    return len(test_scheme)

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()

