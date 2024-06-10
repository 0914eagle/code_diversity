
def can_buy(A, B, C):
    return A + B >= C

def main():
    A, B, C = map(int, input().split())
    if can_buy(A, B, C):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

