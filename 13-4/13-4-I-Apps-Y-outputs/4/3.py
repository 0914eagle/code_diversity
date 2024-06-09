
def get_bonded_base(base):
    if base == "A":
        return "T"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"
    else:
        return "A"

def main():
    base = input()
    print(get_bonded_base(base))

if __name__ == '__main__':
    main()

