def is_happy(s):
    
    if len(s) < 3:
        return False
    if len(s) % 3 != 0:
        return False
    if len(set(s)) == len(s):
        return True
    return False


if __name__ == '__main__':
    print