
def meow_factor(string):
    # Initialize a dictionary to store the meow factor for each prefix of the string
    meow_factors = {}
    
    # Initialize the meow factor for the empty string as 0
    meow_factors[""] = 0
    
    # Loop through each prefix of the string
    for i in range(len(string)):
        # Get the prefix of length i
        prefix = string[:i+1]
        
        # If the prefix contains "meow" as a substring, set the meow factor to 0
        if "meow" in prefix:
            meow_factors[prefix] = 0
        
        # Otherwise, find the minimum meow factor of all prefixes of length i-1 and add 1 to it
        else:
            meow_factors[prefix] = 1 + min(meow_factors[prefix[:-1]] for prefix in prefixes if prefix in meow_factors)
    
    # Return the meow factor of the entire string
    return meow_factors[string]

def main():
    string = input("Enter a string: ")
    print(meow_factor(string))

if __name__ == '__main__':
    main()

