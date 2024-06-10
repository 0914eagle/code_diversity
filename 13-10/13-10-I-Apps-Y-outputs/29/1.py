
def get_input():
    return input()

def convert_case(alpha):
    if alpha.isupper():
        return "A"
    else:
        return "a"

def main():
    alpha = get_input()
    result = convert_case(alpha)
    print(result)

if __name__ == '__main__':
    main()

