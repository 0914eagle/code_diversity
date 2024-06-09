
def get_simplicity(s):
    return len(set(s))

def get_min_erase(s):
    simplicity = get_simplicity(s)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

def main():
    s = input()
    print(get_min_erase(s))

if __name__ == '__main__':
    main()

