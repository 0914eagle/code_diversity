
def read_input():
    return input().strip()

def compare_numbers(a, b):
    if a == b:
        return "="
    elif a < b:
        return "<"
    else:
        return ">"

def main():
    a = read_input()
    b = read_input()
    print(compare_numbers(a, b))

if __name__ == '__main__':
    main()

