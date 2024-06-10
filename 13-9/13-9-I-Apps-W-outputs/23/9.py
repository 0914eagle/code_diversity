
def get_good_strings(s):
    # Initialize a list to store the good strings
    good_strings = []
    
    # Iterate through the characters of the input string
    for i in range(len(s)):
        # If the current character is 1, append it to the list of good strings
        if s[i] == "1":
            good_strings.append("1")
        # If the current character is 0, append it to the list of good strings
        elif s[i] == "0":
            good_strings.append("0")
    
    # Return the list of good strings
    return good_strings

def get_minimal_cuts(s):
    # Get the list of good strings
    good_strings = get_good_strings(s)
    
    # Initialize a variable to store the minimum number of cuts
    min_cuts = len(good_strings)
    
    # Initialize a variable to store the current number of cuts
    current_cuts = 0
    
    # Iterate through the characters of the input string
    for i in range(len(s)):
        # If the current character is 1, increment the current number of cuts
        if s[i] == "1":
            current_cuts += 1
        # If the current character is 0, decrement the current number of cuts
        elif s[i] == "0":
            current_cuts -= 1
        
        # If the current number of cuts is less than the minimum number of cuts, update the minimum number of cuts
        if current_cuts < min_cuts:
            min_cuts = current_cuts
    
    # Return the minimum number of cuts
    return min_cuts

def get_cut_strings(s, min_cuts):
    # Get the list of good strings
    good_strings = get_good_strings(s)
    
    # Initialize a list to store the cut strings
    cut_strings = []
    
    # Initialize a variable to store the current number of cuts
    current_cuts = 0
    
    # Iterate through the characters of the input string
    for i in range(len(s)):
        # If the current character is 1, increment the current number of cuts
        if s[i] == "1":
            current_cuts += 1
        # If the current character is 0, decrement the current number of cuts
        elif s[i] == "0":
            current_cuts -= 1
        
        # If the current number of cuts is equal to the minimum number of cuts, append the current string to the list of cut strings
        if current_cuts == min_cuts:
            cut_strings.append(s[i])
    
    # Return the list of cut strings
    return cut_strings

def main():
    # Input the length of the string
    n = int(input())
    
    # Input the string
    s = input()
    
    # Get the minimum number of cuts
    min_cuts = get_minimal_cuts(s)
    
    # Get the list of cut strings
    cut_strings = get_cut_strings(s, min_cuts)
    
    # Print the number of cuts
    print(len(cut_strings))
    
    # Print the cut strings
    for i in range(len(cut_strings)):
        print(cut_strings[i], end=" ")

if __name__ == '__main__':
    main()

