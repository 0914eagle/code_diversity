def is_happy(s):
    
    if len(s) < 3:
        return False
    if len(s) % 3 != 0:
        return False
    if len(set(s)) != len(s):
        return False
    return True


if __name__ == '__main__':
    s = "aabb"
    print(is_happy(s))
