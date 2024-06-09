
def find_base(y, l):
    for b in range(y, 10):
        if str(y).isdigit() and int(str(y), b) >= l:
            return b
    return -1

