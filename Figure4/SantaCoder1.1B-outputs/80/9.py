def is_happy(s):
    
    if len(s) < 3:
        return False
    if len(s) % 3 != 0:
        return False
    s = s.lower()
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return False
    return True


if __name__ == '__main__':
    s = "aabb"
    print(is_happy(s))
