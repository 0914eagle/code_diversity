
def get_bonded_base(b):
    if b == "A":
        return "T"
    elif b == "C":
        return "G"
    elif b == "G":
        return "C"
    else:
        return "A"

def main():
    b = input()
    print(get_bonded_base(b))

if __name__ == '__main__':
    main()

