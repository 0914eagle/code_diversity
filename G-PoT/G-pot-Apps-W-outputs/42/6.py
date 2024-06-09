
def make_palindrome(s):
    n = len(s)
    operations = []

    def add_operation(op, i):
        operations.append((op, i))

    def reverse_substring(start, end):
        return s[end-1:start-1:-1]

    def is_palindrome(s):
        return s == s[::-1]

    if not is_palindrome(s):
        for i in range(2, n):
            if s[i-1] != s[n-i]:
                add_operation('R', i)
                s = s[:i-1] + reverse_substring(i, n) + s[i-1:]
                break

        for i in range(2, n):
            if s[i-1] != s[n-i]:
                add_operation('L', i)
                s = s[:n-i] + reverse_substring(i, n) + s[n-i:]
                break

    print(len(operations))
    for op, i in operations:
        print(op, i)

# Read input
s = input().strip()

# Call the function
make_palindrome(s)
