
import sys
import math

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def count_possible_orders(n, a):
    # Initialize the number of possible orders to 1
    num_possible_orders = 1
    
    # Iterate over each person
    for i in range(n):
        # Get the absolute difference of the number of people to the left and right of the current person
        left_diff = a[i]
        right_diff = n - 1 - a[i]
        
        # Calculate the total number of possible orders for the current person
        num_possible_orders_person = left_diff * right_diff
        
        # Update the number of possible orders for the entire group
        num_possible_orders *= num_possible_orders_person
    
    # Return the number of possible orders modulo 10^9+7
    return num_possible_orders % (10**9 + 7)

def main():
    n, a = get_input()
    print(count_possible_orders(n, a))

if __name__ == '__main__':
    main()

