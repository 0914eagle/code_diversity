
def get_simplicity(string):
    return len(set(string))

def get_min_erase_count(string):
    simplicity = get_simplicity(string)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

def main():
    string = input()
    print(get_min_erase_count(string))

if __name__ == '__main__':
    main()

