
def get_input():
    return [int(x) for x in input().split()]

def get_largest_number(a, b):
    return max(a+b, a-b, a*b)

if __name__ == '__main__':
    a, b = get_input()
    print(get_largest_number(a, b))

