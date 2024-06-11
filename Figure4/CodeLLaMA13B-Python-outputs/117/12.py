def select_words(s, n):
    
    # your code here
    return [word for word in s.split() if sum(1 for letter in word if letter not in 'aeiou') == n]


if