
def get_meow_factor(string):
    # Initialize a dictionary to store the meow factor for each substring
    meow_factors = {}
    
    # Initialize the meow factor for the empty string as 0
    meow_factors[""] = 0
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character
        substring = string[i:]
        
        # If the substring contains "meow", set the meow factor to 0
        if "meow" in substring:
            meow_factors[substring] = 0
        
        # Otherwise, loop through each operation and calculate the meow factor for the resulting substring
        else:
            for j in range(len(substring)):
                # Insert an arbitrary character into the substring
                substring_insert = substring[:j] + "a" + substring[j:]
                meow_factors[substring_insert] = 1 + meow_factors[substring]
                
                # Delete an arbitrary character from the substring
                substring_delete = substring[:j] + substring[j+1:]
                meow_factors[substring_delete] = 1 + meow_factors[substring]
                
                # Replace any character in the substring by an arbitrary character
                substring_replace = substring[:j] + "a" + substring[j+1:]
                meow_factors[substring_replace] = 1 + meow_factors[substring]
                
                # Swap any two adjacent characters in the substring
                if j > 0:
                    substring_swap = substring[:j-1] + substring[j:j+2][::-1] + substring[j+2:]
                    meow_factors[substring_swap] = 1 + meow_factors[substring]
    
    # Return the meow factor for the original string
    return meow_factors[string]

def main():
    string = input("Enter a string: ")
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

