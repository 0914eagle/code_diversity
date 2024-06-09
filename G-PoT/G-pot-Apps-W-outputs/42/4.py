
def make_palindrome(s):
    n = len(s)
    operations = []
    
    def add_operation(op, i):
        operations.append(f"{op} {i}")
    
    def reverse_substring(start, end):
        return s[end-1:start-1:-1]
    
    def is_palindrome(string):
        return string == string[::-1]
    
    if is_palindrome(s):
        return 0, []
    
    for i in range(2, n):
        if s[i-1] != s[-i]:
            add_operation('R', i)
            s += reverse_substring(i, n)
            break
    
    for i in range(2, n):
        if s[i-1] != s[-i]:
            add_operation('L', i)
            s = reverse_substring(1, i) + s
            break
    
    return len(operations), operations

# Input
s = input().strip()

# Output
k, operations = make_palindrome(s)
print(k)
for op in operations:
    print(op)
