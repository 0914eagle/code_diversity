
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        return -1
    
    # Check if the word can be divided into two halves with equal length
    if len(word) % 2 == 1:
        return -1
    
    # Check if the two halves are anagrams of each other
    half1 = word[:len(word)//2]
    half2 = word[len(word)//2:]
    if sorted(half1) == sorted(half2):
        return half1
    
    return -1

