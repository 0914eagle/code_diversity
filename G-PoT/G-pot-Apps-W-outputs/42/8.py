
def make_palindrome(s):
    n = len(s)
    operations = []

    def add_operation(op, i):
        operations.append((op, i))

    def reverse_substring(start, end):
        return s[end-1:start-2:-1]

    def is_palindrome(string):
        return string == string[::-1]

    if not is_palindrome(s):
        for i in range(2, n):
            if s[i-1] != s[n-i]:
                add_operation('R', i)
                s += reverse_substring(i, n)
                break

        if not is_palindrome(s):
            for i in range(2, n):
                if s[i-1] != s[n-i]:
                    add_operation('L', i)
                    s = reverse_substring(i, n) + s
                    break

    print(len(operations))
    for op, i in operations:
        print(op, i)

# Read input
s = input().strip()

# Call the function
make_palindrome(s)
