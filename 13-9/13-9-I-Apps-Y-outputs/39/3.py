
def get_input():
    return list(map(int, input().split()))

def is_possible(A, B, C):
    for i in range(A, B+1):
        if (i*A) % B == C:
            return "YES"
    return "NO"

def main():
    A, B, C = get_input()
    print(is_possible(A, B, C))

if __name__ == '__main__':
    main()

