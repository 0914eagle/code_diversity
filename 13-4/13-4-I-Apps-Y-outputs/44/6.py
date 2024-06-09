
def get_simplity(string):
    return len(set(string))

def get_min_erase(string):
    simplicity = get_simplity(string)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

def main():
    string = input()
    print(get_min_erase(string))

if __name__ == '__main__':
    main()

