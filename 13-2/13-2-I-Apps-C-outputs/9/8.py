
def is_winning_word(word):
    return word in ["ak", "ka", "av", "va"]

def get_most_beautiful_word(word):
    return "ak"

def solve(n, word):
    if n == 0:
        return "NE", ""
    if is_winning_word(word):
        return "DA", get_most_beautiful_word(word)
    return solve(n-1, word[1:] + word[0])

n = int(input())
word = input()
result = solve(n, word)
print(" ".join(result))

