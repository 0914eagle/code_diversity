
def solve(numbers):
    # split the input string into a list of integers
    numbers = [int(x) for x in numbers.split()]
    # sort the list in ascending order
    numbers.sort()
    # check if the numbers can be added to equal the target
    if numbers[0] + numbers[1] == numbers[2]:
        return f"{numbers[0]} + {numbers[1]} = {numbers[2]}"
    # check if the numbers can be subtracted to equal the target
    if numbers[0] - numbers[1] == numbers[2]:
        return f"{numbers[0]} - {numbers[1]} = {numbers[2]}"
    # check if the numbers can be multiplied to equal the target
    if numbers[0] * numbers[1] == numbers[2]:
        return f"{numbers[0]} * {numbers[1]} = {numbers[2]}"
    # check if the numbers can be divided to equal the target
    if numbers[0] / numbers[1] == numbers[2]:
        return f"{numbers[0]} / {numbers[1]} = {numbers[2]}"
    # if no solution is found, return None
    return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    solution = solve(numbers)
    if solution:
        print(solution)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()

