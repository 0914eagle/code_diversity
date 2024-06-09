
def get_max_problems(n, a):
    # Sort the array of topics in descending order
    a.sort(reverse=True)
    # Initialize variables to keep track of the current topic and the number of problems
    curr_topic = a[0]
    num_problems = 1
    max_problems = 0
    # Iterate through the array of topics
    for i in range(1, n):
        # If the current topic is the same as the previous topic, add the number of problems
        if a[i] == curr_topic:
            num_problems += 1
        # If the current topic is different from the previous topic, add the number of problems to the maximum and reset the number of problems
        else:
            max_problems = max(max_problems, num_problems)
            curr_topic = a[i]
            num_problems = 1
    # Add the number of problems for the last topic
    max_problems = max(max_problems, num_problems)
    return max_problems

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_problems(n, a))

