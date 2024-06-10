
def get_simplicity(s):
    return len(set(s))

def erase_letters(s):
    simplicity = get_simplicity(s)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

if __name__ == '__main__':
    s = input()
    print(erase_letters(s))

