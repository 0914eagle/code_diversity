
def get_maximum_prettiness(problems):
    # Sort the problems in descending order of prettiness
    problems.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    maximum_prettiness = 0
    # Loop through the problems and find the maximum prettiness
    for i in range(len(problems)):
        for j in range(i+1, len(problems)):
            for k in range(j+1, len(problems)):
                # Check if the prettiness of the current problem is divisible by the prettiness of the other two problems
                if problems[i] % problems[j] == 0 and problems[i] % problems[k] == 0:
                    continue
                if problems[j] % problems[i] == 0 and problems[j] % problems[k] == 0:
                    continue
                if problems[k] % problems[i] == 0 and problems[k] % problems[j] == 0:
                    continue
                # If the prettiness of the current problem is not divisible by the prettiness of the other two problems, add it to the maximum prettiness
                maximum_prettiness += problems[i]
    return maximum_prettiness

def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        problems = list(map(int, input().split()))
        print(get_maximum_prettiness(problems))

if __name__ == '__main__':
    main()

