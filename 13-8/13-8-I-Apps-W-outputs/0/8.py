
def get_charges(n, c, t):
    # Initialize a list to store the charges of Grigory's stones
    charges = [0] * n
    # Initialize a list to store the charges of Andrew's stones
    target_charges = [0] * n

    # Loop through each stone and check if the charge is equal to the target charge
    for i in range(n):
        if c[i] != t[i]:
            # If the charge is not equal to the target charge, return "No"
            return "No"

    # If all charges are equal to the target charges, return "Yes"
    return "Yes"

def main():
    # Read the number of magic stones
    n = int(input())
    # Read the charges of Grigory's stones
    c = list(map(int, input().split()))
    # Read the charges of Andrew's stones
    t = list(map(int, input().split()))

    # Call the get_charges function and print the result
    print(get_charges(n, c, t))

if __name__ == '__main__':
    main()

