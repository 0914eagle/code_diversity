
def get_maximum_income(incomes, k):
    # Sort the incomes in non-decreasing order
    incomes.sort()
    # Initialize the total income and the number of changes made
    total_income = 0
    changes_made = 0
    # Iterate through the incomes and make changes
    for i in range(len(incomes)):
        # If we have made all the required changes, break the loop
        if changes_made == k:
            break
        # If the current income is negative, flip its sign and increase the total income
        if incomes[i] < 0:
            incomes[i] = -incomes[i]
            total_income += incomes[i]
            changes_made += 1
    # Return the maximum total income
    return total_income

def main():
    # Read the input
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    # Call the function to get the maximum total income
    maximum_income = get_maximum_income(incomes, k)
    # Print the result
    print(maximum_income)

if __name__ == '__main__':
    main()

