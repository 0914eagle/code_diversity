
def make_palindrome(s):
    n = len(s)
    operations = []

    def add_operation(op, i):
        operations.append((op, i))

    def reverse_substr(start, end):
        return s[end:start-1:-1]

    def is_palindrome(string):
        return string == string[::-1]

    if not is_palindrome(s):
        for i in range(2, n):
            if s[i-1] != s[n-i]:
                add_operation('R', i)
                s = s[:i-1] + reverse_substr(i, n-1) + s[n-1]
                if is_palindrome(s):
                    break

        if not is_palindrome(s):
            for i in range(2, n):
                if s[i-1] != s[n-i]:
                    add_operation('L', i)
                    s = s[0] + reverse_substr(1, i) + s[i:]
                    if is_palindrome(s):
                        break

    print(len(operations))
    for op, i in operations:
        print(op, i)

# Input
s = input().strip()
make_palindrome(s)
