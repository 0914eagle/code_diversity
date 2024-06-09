
def f1(n, m, t, op):
    # Initialize a list to store the possible solutions
    solutions = []
    
    # Iterate over all possible combinations of numbers in the section
    for nums in itertools.combinations(range(1, n+1), m):
        # Check if the combination satisfies the target value and arithmetic operator
        if solve_section(nums, t, op):
            # If it does, add it to the list of solutions
            solutions.append(nums)
    
    # Return the number of solutions
    return len(solutions)

def solve_section(nums, t, op):
    # Check if the target value is reached using the numbers and arithmetic operator
    if op == '+':
        return sum(nums) == t
    elif op == '-':
        return nums[0] - nums[1] == t
    elif op == '*':
        return nums[0] * nums[1] == t
    else:
        return nums[0] / nums[1] == t

if __name__ == '__main__':
    n, m, t, op = map(int, input().split())
    print(f1(n, m, t, op))

