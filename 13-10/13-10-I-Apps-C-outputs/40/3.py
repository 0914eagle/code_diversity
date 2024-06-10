
def read_input():
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    return N, C, a, b, Q

def get_number_of_purchases(N, C, a, b, Q):
    # Initialize the number of purchases with 1, since each client must purchase at least one painting
    num_purchases = 1
    
    # Loop through each requirement change
    for _ in range(Q):
        # Read the input for the requirement change
        P, a_P, b_P = map(int, input().split())
        
        # Update the number of purchases based on the new requirements
        num_purchases = max(num_purchases, a_P + b_P + 1)
    
    # Return the number of purchases modulo 10007
    return num_purchases % 10007

def main():
    N, C, a, b, Q = read_input()
    print(get_number_of_purchases(N, C, a, b, Q))

if __name__ == '__main__':
    main()

