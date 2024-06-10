
import sys

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def get_possible_orders(N, A):
    # Initialize a list to store the possible orders
    orders = []
    
    # Iterate over each possible order
    for i in range(1, N+1):
        # Check if the current order is consistent with the reports
        if is_consistent(N, A, i):
            # If it is, add it to the list of possible orders
            orders.append(i)
    
    # Return the list of possible orders
    return orders

def is_consistent(N, A, order):
    # Initialize a flag to indicate if the order is consistent
    consistent = True
    
    # Iterate over each person in the order
    for i in range(N):
        # Get the number of people to the left and right of the current person
        left = order - i - 1
        right = N - order - i - 1
        
        # Check if the current person's report is consistent with the number of people to the left and right
        if left < 0 or left != A[i] or right < 0 or right != A[N-i-1]:
            # If it is not, set the flag to False and break the loop
            consistent = False
            break
    
    # Return the flag
    return consistent

def main():
    # Get the input
    N, A = get_input()
    
    # Get the possible orders
    orders = get_possible_orders(N, A)
    
    # Print the number of possible orders
    print(len(orders))

if __name__ == '__main__':
    main()

