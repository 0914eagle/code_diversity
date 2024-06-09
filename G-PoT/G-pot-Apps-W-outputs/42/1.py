
def make_palindrome(s):
    n = len(s)
    operations = []

    def append_front(i):
        operations.append(f"L {i}")
        return s[i-1::-1] + s

    def append_end(i):
        operations.append(f"R {i}")
        return s + s[n-i:][::-1]

    if s != s[::-1]:
        for i in range(2, n):
            if s[i:] == s[i:][::-1]:
                s = append_end(i)
                break
            elif s[:n-i] == s[:n-i][::-1]:
                s = append_front(i)
                break

    while s != s[::-1]:
        for i in range(2, n):
            if s[i:] == s[i:][::-1]:
                s = append_end(i)
                break
            elif s[:n-i] == s[:n-i][::-1]:
                s = append_front(i)
                break

    print(len(operations))
    for op in operations:
        print(op)

# Input
s = input().strip()

make_palindrome(s)
