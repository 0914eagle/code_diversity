
def get_input():
    return list(map(int, input().split()))

def calculate_largest_value(a, b):
    return max(a+b, a-b, a*b)

def main():
    a, b = get_input()
    largest_value = calculate_largest_value(a, b)
    print(largest_value)

if __name__ == '__main__':
    main()

