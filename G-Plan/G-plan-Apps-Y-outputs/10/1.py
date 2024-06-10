
def calculate_remaining_amount(X, A, B):
    remaining_after_cake = X - A
    remaining_after_donuts = remaining_after_cake % B
    return remaining_after_donuts

if __name__ == "__main__":
    X = int(input())
    A = int(input())
    B = int(input())
    
    result = calculate_remaining_amount(X, A, B)
    print(result)
