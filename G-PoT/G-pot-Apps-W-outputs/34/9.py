
def check_banner(word):
    target = "CODEFORCES"
    n = len(word)
    m = len(target)
    
    for i in range(n):
        if word[i:i+m] == target:
            return "YES"
    
    for i in range(1, n):
        if word[:i] + word[i+m:] == target:
            return "YES"
    
    return "NO"

# Read input
word = input().strip()

# Check if it's possible to cut out a substring to form "CODEFORCES"
result = check_banner(word)
print(result)
