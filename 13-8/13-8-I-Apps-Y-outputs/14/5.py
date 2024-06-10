
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_possible_orders(n, a):
    # Initialize a dictionary to store the number of possible orders for each person
    possible_orders = {i: 0 for i in range(1, n + 1)}

    # Initialize a set to store the possible orders
    orders = set()

    # Iterate through each person and their report
    for i in range(1, n + 1):
        # Get the difference between the number of people to the left and right of the current person
        left, right = a[i - 1], n - a[i - 1] - 1

        # If the difference is 0, then the current person can be in any position
        if left == right:
            possible_orders[i] = n

        # If the difference is 1, then the current person can be in any position except the middle
        elif left == right - 1:
            possible_orders[i] = n - 1

        # If the difference is greater than 1, then the current person can be in any position except the positions on either side
        else:
            possible_orders[i] = n - left - right

    # Iterate through each person and their possible orders
    for i in range(1, n + 1):
        # Get the possible orders for the current person
        current_orders = possible_orders[i]

        # If the current person is in the first position, then they can be in any position
        if i == 1:
            orders |= set(range(1, current_orders + 1))

        # If the current person is in the last position, then they can be in any position except the first
        elif i == n:
            orders |= set(range(current_orders, n + 1))

        # If the current person is in any other position, then they can be in any position except the positions on either side
        else:
            orders |= set(range(i - current_orders, i + current_orders + 1))

    # Return the number of possible orders modulo 10^9 + 7
    return len(orders) % (10**9 + 7)

def main():
    n, a = get_input()
    print(get_possible_orders(n, a))

if __name__ == '__main__':
    main()

