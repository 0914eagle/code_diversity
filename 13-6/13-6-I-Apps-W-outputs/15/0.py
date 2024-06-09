
def get_maximum_income(incomes, k):
    # Sort the incomes in non-decreasing order
    incomes.sort()
    
    # Initialize the total income and the number of changes made
    total_income = sum(incomes)
    num_changes = k
    
    # Iterate through the incomes and change the sign of each income
    for i in range(len(incomes)):
        # If the income is positive, change it to negative
        if incomes[i] > 0:
            incomes[i] *= -1
            num_changes -= 1
        # If the income is negative, change it to positive
        elif incomes[i] < 0:
            incomes[i] *= -1
            num_changes -= 1
    
    # Return the maximum total income after making exactly k changes
    return total_income

def main():
    # Read the input n and k
    n, k = map(int, input().split())
    
    # Read the incomes
    incomes = list(map(int, input().split()))
    
    # Get the maximum total income
    maximum_income = get_maximum_income(incomes, k)
    
    # Print the maximum total income
    print(maximum_income)

if __name__ == '__main__':
    main()

