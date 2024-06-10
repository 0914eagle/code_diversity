
def count_upper(s: str) -> int:
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

s = input().strip()
print(count_upper(s))
