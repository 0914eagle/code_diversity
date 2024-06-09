
def solve(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return 0
    
    # Initialize the minimum number of hugs needed to make the string palindromic
    min_hugs = float('inf')
    
    # Loop through each character of the string
    for i in range(len(s)):
        # Check if the character is different from its mirrored character
        if s[i] != s[len(s) - i - 1]:
            # Calculate the number of hugs needed to make the string palindromic by changing this character
            hugs = 1 + solve(s[:i] + s[len(s) - i - 1] + s[i + 1:])
            
            # Update the minimum number of hugs needed
            min_hugs = min(min_hugs, hugs)
    
    return min_hugs

