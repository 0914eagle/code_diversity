
def calculate_remaining_amount(X, A, B):
    remaining_after_cake = X - A
    num_donuts = remaining_after_cake // B
    remaining_amount = remaining_after_cake - (num_donuts * B)
    return remaining_amount

if __name__ == "__main__":
    X = int(input())
    A = int(input())
    B = int(input())
    result = calculate_remaining_amount(X, A, B)
    print(result)
