
def get_max_cumulative_prettiness(problems):
    # Sort the problems in non-decreasing order of their prettiness
    problems.sort()
    # Initialize the maximum cumulative prettiness to be 0
    max_cumulative_prettiness = 0
    # Iterate over the first three problems
    for i in range(3):
        # If the current problem is not divisible by the previous two problems, add its prettiness to the cumulative sum
        if i == 0 or (problems[i] % problems[i-1] != 0 and problems[i] % problems[i-2] != 0):
            max_cumulative_prettiness += problems[i]
    return max_cumulative_prettiness

def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        problems = list(map(int, input().split()))
        print(get_max_cumulative_prettiness(problems))

if __name__ == '__main__':
    main()

