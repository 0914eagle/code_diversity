
def get_input():
    return list(map(int, input().split()))

def is_possible(A, B, C):
    for i in range(A, 101):
        if i % A == C:
            return True
    return False

def main():
    A, B, C = get_input()
    if is_possible(A, B, C):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

