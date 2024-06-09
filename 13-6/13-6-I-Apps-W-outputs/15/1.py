
def get_max_income(incomes, k):
    # Sort the incomes in non-decreasing order
    incomes.sort()
    
    # Initialize the total income and the number of changes made
    total_income = 0
    num_changes = 0
    
    # Iterate through the incomes and make changes if possible
    for i in range(len(incomes)):
        # If the number of changes made is less than k, make a change
        if num_changes < k:
            # If the current income is negative, change its sign
            if incomes[i] < 0:
                incomes[i] = -incomes[i]
                num_changes += 1
        # Add the current income to the total income
        total_income += incomes[i]
    
    # Return the maximum total income
    return total_income

def main():
    # Read the input
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    
    # Get the maximum total income
    max_income = get_max_income(incomes, k)
    
    # Print the result
    print(max_income)

if __name__ == '__main__':
    main()

