
def can_form_codeforces(word):
    target = "CODEFORCES"
    n = len(word)
    
    for i in range(n):
        for j in range(i, n):
            new_word = word[:i] + word[j+1:]
            if new_word == target:
                return "YES"
    
    return "NO"

# Read input
word = input().strip()

# Check if it is possible to form CODEFORCES
result = can_form_codeforces(word)
print(result)
