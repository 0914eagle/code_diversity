
import itertools

def get_meow_factor(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Iterate over all possible substrings of length 3 in the string
    for i in range(len(s) - 2):
        # Check if the substring is "meow"
        if s[i:i+3] == "meo":
            # If it is, return the meow factor
            return meow_factor
        # If it is not, increment the meow factor
        meow_factor += 1
    
    # If no substring of length 3 is "meow", return -1
    return -1

def get_all_meow_factors(s):
    # Initialize a list to store the meow factors
    meow_factors = []
    
    # Iterate over all possible substrings of length 3 in the string
    for i in range(len(s) - 2):
        # Check if the substring is "meow"
        if s[i:i+3] == "meo":
            # If it is, add the meow factor to the list
            meow_factors.append(i)
    
    # Return the list of meow factors
    return meow_factors

if __name__ == '__main__':
    s = input()
    print(get_meow_factor(s))
    print(get_all_meow_factors(s))

