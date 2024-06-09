
def get_position(n, k, initial_strings, test_string):
    # create a list of all possible composite strings
    composite_strings = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                composite_strings.append(initial_strings[i] + initial_strings[j] + initial_strings[k])
    
    # sort the list of composite strings in alphabetical order
    composite_strings.sort()
    
    # find the position of the test string in the sorted list
    position = composite_strings.index(test_string) + 1
    
    # return the position modulo 10^9 + 7
    return position % (10**9 + 7)

