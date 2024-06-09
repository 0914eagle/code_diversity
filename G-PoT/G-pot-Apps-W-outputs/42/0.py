
s = input()
n = len(s)

def is_palindrome(s):
    return s == s[::-1]

operations = []

if not is_palindrome(s):
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            operations.append(f"R {i}")
            s = s[:i] + s[i-1:n][::-1] + s[n-i:]
    
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            operations.append(f"L {i}")
            s = s[:i-1] + s[i-1:n][::-1] + s[n-i+1:]

print(len(operations))
for op in operations:
    print(op)
