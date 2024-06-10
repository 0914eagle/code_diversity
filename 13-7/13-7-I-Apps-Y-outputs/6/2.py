
def get_bonded_base(b):
    bonded_base = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A"
    }
    return bonded_base[b]

def main():
    b = input()
    print(get_bonded_base(b))

if __name__ == '__main__':
    main()

