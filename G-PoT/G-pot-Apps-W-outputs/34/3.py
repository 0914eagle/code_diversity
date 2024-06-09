
def can_form_codeforces(word):
    target_word = "CODEFORCES"
    n = len(word)
    m = len(target_word)

    for i in range(n):
        for j in range(i, n):
            new_word = word[:i] + word[j+1:]
            if len(new_word) == m and new_word == target_word:
                return "YES"
    
    return "NO"

# Read input
word = input().strip()

# Check if it is possible to cut out a substring to form "CODEFORCES"
result = can_form_codeforces(word)
print(result)
