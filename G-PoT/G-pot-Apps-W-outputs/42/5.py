
def make_palindrome(s):
    n = len(s)
    operations = []
    
    def add_operation(op, i):
        operations.append((op, i))
    
    def reverse_substring(start, end):
        return s[end-1:start-2:-1]
    
    def is_palindrome(string):
        return string == string[::-1]
    
    if is_palindrome(s):
        return 0, []
    
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            add_operation('R', i)
            s = s[:i] + reverse_substring(i, n) + s[i:]
            break
    
    for i in range(2, n):
        if s[i-1] != s[n-i]:
            add_operation('L', i)
            s = s[:i-1] + reverse_substring(i, n) + s[i-1:]
            break
    
    return len(operations), operations

# Input
s = input().strip()

# Output
k, operations = make_palindrome(s)
print(k)
for op, i in operations:
    print(f"{op} {i}")
