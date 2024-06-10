
def count_upper(s: str) -> int:
    vowels = set('AEIOU')
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

# Input reading and function invocation
s = input().strip()
print(count_upper(s))
