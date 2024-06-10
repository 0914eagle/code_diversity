
def calculate_remaining_amount(X, A, B):
    remaining_amount = X - A
    remaining_amount -= (remaining_amount // B) * B
    return remaining_amount

if __name__ == "__main__":
    X = int(input())
    A = int(input())
    B = int(input())
    result = calculate_remaining_amount(X, A, B)
    print(result)
