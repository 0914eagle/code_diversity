
s = input().strip()

def make_palindrome(s):
    operations = []
    n = len(s)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    if is_palindrome(s):
        return 0, operations
    
    for i in range(2, n):
        if s[i:] == s[i:][::-1]:
            operations.append(('R', i))
            s = s[:i] + s[i:][::-1]
            break
    
    for i in range(2, n):
        if s[:n-i] == s[:n-i][::-1]:
            operations.append(('L', n-i))
            s = s[:n-i] + s
            break
    
    return len(operations), operations

k, operations = make_palindrome(s)
print(k)
for op in operations:
    print(op[0], op[1])
