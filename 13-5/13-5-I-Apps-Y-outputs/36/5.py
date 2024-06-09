
def get_input():
    return input()

def replace_digits(n):
    n = list(n)
    for i in range(len(n)):
        if n[i] == "1":
            n[i] = "9"
        elif n[i] == "9":
            n[i] = "1"
    return "".join(n)

def main():
    n = get_input()
    print(replace_digits(n))

if __name__ == '__main__':
    main()

