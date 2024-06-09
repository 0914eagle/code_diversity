
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        return -1
    
    # Check if the word can be divided into two halves
    half = len(word) // 2
    if word[:half] == word[half:][::-1]:
        return word[:half]
    
    # Check if the word can be divided into three halves
    third = len(word) // 3
    if word[:third] == word[third:][::-1] == word[2*third:][::-1]:
        return word[:third]
    
    # Check if the word can be divided into four halves
    fourth = len(word) // 4
    if word[:fourth] == word[fourth:][::-1] == word[2*fourth:][::-1] == word[3*fourth:][::-1]:
        return word[:fourth]
    
    # If none of the above conditions are met, the word is not a multigram
    return -1

