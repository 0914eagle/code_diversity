
def can_buy_toy(A, B, C):
    total = A + B
    if total >= C:
        return "Yes"
    else:
        return "No"

def main():
    A, B, C = map(int, input().split())
    print(can_buy_toy(A, B, C))

if __name__ == '__main__':
    main()

