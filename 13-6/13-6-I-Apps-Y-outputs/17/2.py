
def get_input():
    return list(map(int, input().split()))

def largest_value(a, b):
    return max(a+b, a-b, a*b)

if __name__ == '__main__':
    a, b = get_input()
    print(largest_value(a, b))

