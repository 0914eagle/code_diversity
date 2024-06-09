
def get_max_problems(n, a):
    # Sort the array of topics in descending order
    a.sort(reverse=True)
    # Initialize variables to keep track of the current topic and the number of problems
    current_topic = a[0]
    num_problems = 1
    max_problems = 0
    # Iterate through the array of topics
    for i in range(1, n):
        # If the current topic is the same as the previous topic, add the number of problems
        if a[i] == current_topic:
            num_problems += 1
        # If the current topic is different from the previous topic, update the current topic and the number of problems
        else:
            current_topic = a[i]
            num_problems = 1
        # Update the maximum number of problems if necessary
        max_problems = max(max_problems, num_problems)
    return max_problems

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_problems(n, a))

