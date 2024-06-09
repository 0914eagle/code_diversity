
def solve(string1, string2):
    # Find all subpairs of string1 and string2
    subpairs1 = find_subpairs(string1)
    subpairs2 = find_subpairs(string2)
    
    # Initialize the maximum length and palindrome strings
    max_length = 0
    palindrome = ""
    
    # Iterate over each subpair of string1 and string2
    for subpair1 in subpairs1:
        for subpair2 in subpairs2:
            # Concatenate the subpairs
            concatenated = subpair1[0] + subpair1[1] + subpair2[0] + subpair2[1]
            
            # Check if the concatenated string is a palindrome
            if is_palindrome(concatenated):
                # Check if the length of the concatenated string is greater than the current maximum length
                if len(concatenated) > max_length:
                    # Update the maximum length and palindrome strings
                    max_length = len(concatenated)
                    palindrome = concatenated
    
    # Return the maximum length of the palindrome
    return max_length

def find_subpairs(string):
    # Initialize an empty list to store the subpairs
    subpairs = []
    
    # Iterate over each substring of the string
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            # Add the substring to the list of subpairs
            subpairs.append((string[i:j], string[j:]))
    
    # Return the list of subpairs
    return subpairs

def is_palindrome(string):
    # Check if the string is a palindrome
    return string == string[::-1]

