
def make_palindrome(s):
    operations = []
    n = len(s)
    
    def add_operation(op, i):
        operations.append((op, i))
    
    def reverse_substring(start, end):
        return s[end-1:start-1:-1]
    
    def is_palindrome(string):
        return string == string[::-1]
    
    if is_palindrome(s):
        return 0, operations
    
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            add_operation('R', i)
            s += reverse_substring(i, n)
            break
    
    if is_palindrome(s):
        return 1, operations
    
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            add_operation('L', i)
            s = reverse_substring(i, n) + s
            break
    
    return 2, operations

# Input
s = input().strip()

# Output
k, operations = make_palindrome(s)
print(k)
for op, i in operations:
    print(op, i)
