
def get_input():
    return [int(x) for x in input().split()]

def calculate_largest_number(a, b):
    return max(a + b, a - b, a * b)

def main():
    a, b = get_input()
    print(calculate_largest_number(a, b))

if __name__ == '__main__':
    main()

