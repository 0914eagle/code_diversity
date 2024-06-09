
def check_banner(word):
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

# Check if it's possible to cut out a substring to form "CODEFORCES"
result = check_banner(word)
print(result)
