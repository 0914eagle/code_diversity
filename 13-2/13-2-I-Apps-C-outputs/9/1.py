
def is_winning_word(word):
    return word in ["ak", "ka"]

def get_most_beautiful_word(word):
    return "ak" if word in ["ak", "ka"] else "ka"

def solve(n, word):
    if n == 0:
        return "NE", ""
    if n == 1:
        return "DA", word
    if is_winning_word(word):
        return "DA", get_most_beautiful_word(word)
    return solve(n-1, word[1:] + word[0])

n = int(input())
word = input()
result = solve(n, word)
print("DA" if result[0] == "DA" else "NE")
print(result[1])

