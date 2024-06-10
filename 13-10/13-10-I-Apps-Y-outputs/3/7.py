
def get_simplicity(string):
    return len(set(string))

def get_min_erased_letters(string):
    simplicity = get_simplicity(string)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

if __name__ == '__main__':
    string = input()
    print(get_min_erased_letters(string))

