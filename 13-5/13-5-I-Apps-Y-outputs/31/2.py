
def get_input():
    return list(map(int, input().split()))

def find_largest(a, b):
    return max(a+b, a-b, a*b)

if __name__ == '__main__':
    a, b = get_input()
    print(find_largest(a, b))

