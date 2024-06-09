
def get_maximum_income(numbers, k):
    if k == 0:
        return sum(numbers)
    
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the maximum income and the current income
    max_income = 0
    current_income = 0
    
    # Iterate through the numbers and change the sign of the numbers
    for i in range(len(numbers)):
        current_income += numbers[i]
        if current_income > max_income:
            max_income = current_income
        if i < len(numbers) - 1 and numbers[i] < 0 and numbers[i+1] > 0:
            numbers[i] *= -1
            numbers[i+1] *= -1
    
    return max_income

def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_maximum_income(numbers, k))

if __name__ == '__main__':
    main()

