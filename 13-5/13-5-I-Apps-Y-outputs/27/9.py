
import sys

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def f1(n, a):
    # Initialize a dictionary to store the number of possible orders for each person
    num_orders = {i: 0 for i in range(1, n + 1)}
    # Initialize a set to store the possible orders
    orders = set()
    # Iterate through each person and their report
    for i in range(1, n + 1):
        # Get the number of people to the left and right of the current person
        left = i - 1
        right = n - i
        # Check if the report is valid
        if a[i - 1] >= left and a[i - 1] <= right:
            # Get the number of possible orders for the current person
            num_orders[i] = (a[i - 1] + 1) * (right - a[i - 1])
            # Add the current person to the set of possible orders
            for j in range(left, a[i - 1] + 1):
                orders.add((i, j + 1, a[i - 1] + j + 2, a[i - 1] + j + 3))
    # Return the number of possible orders
    return len(orders)

def f2(n, a):
    # Initialize a dictionary to store the number of possible orders for each person
    num_orders = {i: 0 for i in range(1, n + 1)}
    # Initialize a set to store the possible orders
    orders = set()
    # Iterate through each person and their report
    for i in range(1, n + 1):
        # Get the number of people to the left and right of the current person
        left = i - 1
        right = n - i
        # Check if the report is valid
        if a[i - 1] >= left and a[i - 1] <= right:
            # Get the number of possible orders for the current person
            num_orders[i] = (a[i - 1] + 1) * (right - a[i - 1])
            # Add the current person to the set of possible orders
            for j in range(left, a[i - 1] + 1):
                orders.add((i, j + 1, a[i - 1] + j + 2, a[i - 1] + j + 3))
    # Return the number of possible orders
    return len(orders)

if __name__ == '__main__':
    n, a = get_input()
    print(f1(n, a))
    print(f2(n, a))

