
def get_max_income(numbers, k):
    if k == 0:
        return sum(numbers)
    
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the maximum income and the current income
    max_income = 0
    current_income = 0
    
    # Iterate through the numbers and change their signs
    for i in range(len(numbers)):
        current_income += numbers[i]
        max_income = max(max_income, current_income)
        if i < len(numbers) - 1:
            current_income -= numbers[i]
            current_income += -numbers[i]
    
    return max_income

def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_max_income(numbers, k))

if __name__ == '__main__':
    main()

