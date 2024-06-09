
def get_maximum_income(incomes, k):
    # Sort the incomes in non-decreasing order
    incomes.sort()
    # Initialize the total income and the number of swaps
    total_income = 0
    num_swaps = 0
    # Loop through the incomes and perform swaps
    for i in range(len(incomes)):
        # Check if the current income is negative
        if incomes[i] < 0:
            # Perform a swap by multiplying the current income by -1
            incomes[i] *= -1
            # Increment the total income and the number of swaps
            total_income += incomes[i]
            num_swaps += 1
        # Check if the number of swaps is equal to k
        if num_swaps == k:
            # Break the loop
            break
    # Return the total income
    return total_income

def main():
    # Read the input
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    # Call the get_maximum_income function and print the result
    print(get_maximum_income(incomes, k))

if __name__ == '__main__':
    main()

