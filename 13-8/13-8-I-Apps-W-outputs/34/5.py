
def read_numbers():
    return map(int, input().split())

def compare_numbers(a, b):
    if a < b:
        return "<"
    elif a > b:
        return ">"
    else:
        return "="

def main():
    a, b = read_numbers()
    print(compare_numbers(a, b))

if __name__ == '__main__':
    main()

