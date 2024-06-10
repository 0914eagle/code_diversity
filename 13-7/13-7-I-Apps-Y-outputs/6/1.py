
def bond_with(base):
    if base == 'A':
        return 'T'
    elif base == 'C':
        return 'G'
    elif base == 'G':
        return 'C'
    else:
        return 'A'

def main():
    base = input()
    print(bond_with(base))

if __name__ == '__main__':
    main()

