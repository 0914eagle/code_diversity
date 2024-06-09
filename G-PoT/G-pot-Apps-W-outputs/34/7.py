
def can_form_codeforces(word):
    target = "CODEFORCES"
    n = len(word)
    m = len(target)
    
    for i in range(n):
        for j in range(i, n):
            if word[:i] + word[j+1:] == target:
                return "YES"
    
    return "NO"

# Read input
word = input().strip()

# Check if it is possible to form CODEFORCES
result = can_form_codeforces(word)
print(result)
