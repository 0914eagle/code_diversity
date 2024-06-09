
def get_input():
    return list(map(int, input().split()))

def largest_value(A, B):
    return max(A+B, A-B, A*B)

def main():
    A, B = get_input()
    print(largest_value(A, B))

if __name__ == '__main__':
    main()

