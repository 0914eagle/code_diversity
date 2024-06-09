
s = input()
n = len(s)

def is_palindrome(string):
    return string == string[::-1]

operations = []

for i in range(2, n):
    if s[i:] == s[i:][::-1]:
        operations.append("R " + str(i))
        s = s[:i] + s[i:][::-1]
        break

for i in range(2, n):
    if s[:n-i] == s[:n-i][::-1]:
        operations.append("L " + str(n-i))
        s = s[:n-i] + s
        break

print(len(operations))
for op in operations:
    print(op)
