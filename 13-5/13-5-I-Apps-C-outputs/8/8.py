
def f1(n, s):
    # Function to find the length of the longest alternating subsequence
    # in a given string
    def longest_alternating_subsequence(s):
        # Initialize the length of the longest alternating subsequence as 1
        longest = 1
        # Initialize the current length of the alternating subsequence as 1
        current = 1
        # Iterate over the characters of the string
        for i in range(1, len(s)):
            # If the current character is different from the previous character,
            # increment the current length of the alternating subsequence
            if s[i] != s[i-1]:
                current += 1
            # If the current length of the alternating subsequence is greater than
            # the longest alternating subsequence, update the longest alternating subsequence
            if current > longest:
                longest = current
        # Return the length of the longest alternating subsequence
        return longest
    
    # Function to flip a substring of a given string
    def flip_substring(s, start, end):
        # Initialize a new string with the same length as the input string
        new_s = [""] * len(s)
        # Iterate over the characters of the input string
        for i in range(len(s)):
            # If the current character is in the substring to be flipped, flip it
            if start <= i <= end:
                if s[i] == "0":
                    new_s[i] = "1"
                else:
                    new_s[i] = "0"
            # Otherwise, keep the character unchanged
            else:
                new_s[i] = s[i]
        # Return the new string
        return "".join(new_s)
    
    # Initialize the length of the longest alternating subsequence as 0
    longest = 0
    # Iterate over all possible substrings of the input string
    for i in range(n):
        for j in range(i+1, n+1):
            # Flip the current substring and find the length of the longest alternating subsequence
            flipped = flip_substring(s, i, j-1)
            current = longest_alternating_subsequence(flipped)
            # If the current length is greater than the longest alternating subsequence, update it
            if current > longest:
                longest = current
    # Return the length of the longest alternating subsequence
    return longest

def f2(...):
    # Your code here

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

