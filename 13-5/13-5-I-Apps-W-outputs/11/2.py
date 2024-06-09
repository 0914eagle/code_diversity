
def is_divisible_by_x_minus_k(coefficients, k):
    # implement your solution here
    return True

def main():
    n, k = map(int, input().split())
    coefficients = []
    for i in range(n + 1):
        coefficient = input()
        if coefficient == '?':
            coefficients.append(None)
        else:
            coefficients.append(int(coefficient))
    if is_divisible_by_x_minus_k(coefficients, k):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

