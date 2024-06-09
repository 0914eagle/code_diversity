
def get_max_income(numbers, k):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the total income and the number of changes made
    total_income = sum(numbers)
    changes_made = 0
    # Loop through the numbers and change the sign of the numbers until the maximum total income is reached or the maximum number of changes is made
    while changes_made < k:
        for i in range(len(numbers)):
            if numbers[i] < 0:
                numbers[i] = -numbers[i]
                total_income += numbers[i]
                changes_made += 1
                break
    # Return the maximum total income
    return total_income

def main():
    # Read the input data
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    # Get the maximum total income
    max_income = get_max_income(numbers, k)
    # Print the result
    print(max_income)

if __name__ == '__main__':
    main()

