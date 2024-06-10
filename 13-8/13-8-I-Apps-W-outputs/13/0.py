
def get_good_strings(s):
    # Initialize a list to store the good strings
    good_strings = []
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is 1, append it to the current good string
        if s[i] == "1":
            good_strings.append(s[i])
        # If the current character is 0 and the previous character is 1, start a new good string
        elif s[i] == "0" and i > 0 and s[i-1] == "1":
            good_strings.append(s[i])
    
    return good_strings

def get_minimal_cuts(s):
    # Get the list of good strings
    good_strings = get_good_strings(s)
    
    # Initialize a variable to store the minimal number of cuts
    minimal_cuts = len(good_strings)
    
    # Iterate through the good strings
    for i in range(len(good_strings)):
        # If the current string is not the last string, try cutting it in half
        if i < len(good_strings) - 1:
            # Get the length of the current string
            current_string_length = len(good_strings[i])
            
            # If the current string is even, try cutting it in half
            if current_string_length % 2 == 0:
                # Get the length of the first half of the current string
                first_half_length = current_string_length // 2
                
                # Get the first half of the current string
                first_half = good_strings[i][:first_half_length]
                
                # Get the second half of the current string
                second_half = good_strings[i][first_half_length:]
                
                # If both halves are good, update the minimal number of cuts
                if is_good_string(first_half) and is_good_string(second_half):
                    minimal_cuts = min(minimal_cuts, 1 + get_minimal_cuts(first_half + second_half))
            
            # If the current string is odd, try cutting it in half and then in half again
            if current_string_length % 2 == 1:
                # Get the length of the first half of the current string
                first_half_length = (current_string_length - 1) // 2
                
                # Get the first half of the current string
                first_half = good_strings[i][:first_half_length]
                
                # Get the second half of the current string
                second_half = good_strings[i][first_half_length:]
                
                # If both halves are good, update the minimal number of cuts
                if is_good_string(first_half) and is_good_string(second_half):
                    minimal_cuts = min(minimal_cuts, 1 + get_minimal_cuts(first_half + second_half))
    
    return minimal_cuts

def is_good_string(s):
    # Initialize a variable to store the number of 0s
    num_zeros = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is 0, increment the number of 0s
        if s[i] == "0":
            num_zeros += 1
    
    # If the number of 0s is equal to the number of 1s, the string is good
    if num_zeros == len(s) - num_zeros:
        return True
    else:
        return False

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Get the minimal number of cuts
    minimal_cuts = get_minimal_cuts(s)
    
    # Print the result
    print(minimal_cuts)
    print(" ".join(get_good_strings(s)))

if __name__ == '__main__':
    main()

