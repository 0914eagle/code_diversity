def solve(s):
    
    s = s[::-1]
    for i in range(len(s)):
        if s[i].isalpha():
            s = s[:i] + s[i].swapcase() + s[i+1:]
    return s

print(solve("1234"))
print(solve("ab"))
print(solve("#a@C"))
print(solve("123456789"))
print(solve("1234567890"))
print(solve("12345678901"))
print(solve("123456789012"))
print(solve("1234567890123"))
print(solve("12345678901234"))
print(solve("123456789012345"))
print(solve("1234567890123456"))
print(solve("12345678901234567"))
print(solve("123456789012345678"))
print(solve("1234567890123456789"))
print(solve("12345678901234567890"))
print(solve("123456789012345678901"))
print(solve("1234567890123456789012"))
print(solve("12345678901234567890123"))
print(solve("123456789012345678901234"))
print(solve("1234567890123456789012345"))
print(solve("12345678901234567890123456"))
print(solve("12345