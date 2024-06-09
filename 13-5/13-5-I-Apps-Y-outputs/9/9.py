
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        return -1
    
    # Check if the word can be divided into two halves with equal length
    if len(word) % 2 == 1:
        return -1
    
    # Check if the first half is an anagram of the second half
    first_half = word[:len(word)//2]
    second_half = word[len(word)//2:]
    if sorted(first_half) == sorted(second_half):
        return first_half
    
    return -1

