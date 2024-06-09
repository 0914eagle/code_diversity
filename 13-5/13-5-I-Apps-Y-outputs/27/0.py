
import sys

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def count_orders(n, a):
    # Initialize the number of possible orders to 1
    orders = 1
    # Loop through each person
    for i in range(n):
        # Get the number of people to the left and right of the current person
        left, right = i - 1, n - i
        # If the difference between the number of people to the left and right is not equal to the current person's report,
        # then there are no possible orders, so return 0
        if a[i] != abs(left - right):
            return 0
        # Otherwise, multiply the number of possible orders by the number of possible positions for the current person
        orders *= n - i
    # Return the number of possible orders
    return orders

def main():
    n, a = get_input()
    print(count_orders(n, a))

if __name__ == '__main__':
    main()

