
def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) < 3:
            return False

    return True

s = input().strip()
print(is_happy(s))
