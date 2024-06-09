
def get_optimal_subsequence(a, k, pos):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the sum of the subsequence to 0
    sum = 0
    # Initialize the optimal subsequence as an empty list
    opt = []
    # Iterate through the array
    for i in range(len(a)):
        # Add the current element to the subsequence
        opt.append(a[i])
        # Add the current element to the sum
        sum += a[i]
        # If the length of the subsequence is equal to k, break
        if len(opt) == k:
            break
    # Return the element at the given position in the optimal subsequence
    return opt[pos-1]

def solve(a, m):
    # Initialize an empty list to store the answers
    answers = []
    # Iterate through the requests
    for i in range(m):
        # Read the current request
        k, pos = map(int, input().split())
        # Get the optimal subsequence for the current request
        ans = get_optimal_subsequence(a, k, pos)
        # Add the answer to the list of answers
        answers.append(ans)
    # Return the list of answers
    return answers

a = list(map(int, input().split()))
m = int(input())
answers = solve(a, m)
for ans in answers:
    print(ans)

