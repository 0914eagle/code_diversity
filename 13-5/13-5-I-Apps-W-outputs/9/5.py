
def get_cyclic_shifts(word):
    # Initialize an empty list to store the cyclic shifts
    cyclic_shifts = []
    
    # Loop through each position in the word
    for i in range(len(word)):
        # Get the cyclic shift of the word by moving the last character to the beginning
        cyclic_shift = word[i:] + word[:i]
        
        # Add the cyclic shift to the list if it is not already in the list
        if cyclic_shift not in cyclic_shifts:
            cyclic_shifts.append(cyclic_shift)
    
    return cyclic_shifts

def count_distinct_words(word):
    # Get all the cyclic shifts of the word
    cyclic_shifts = get_cyclic_shifts(word)
    
    # Return the number of distinct cyclic shifts
    return len(set(cyclic_shifts))

if __name__ == '__main__':
    word = input()
    print(count_distinct_words(word))

