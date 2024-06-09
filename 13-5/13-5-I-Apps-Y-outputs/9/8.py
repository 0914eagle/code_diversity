
def f1(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # initialize the number of problems to be included in the contest
    num_problems = 1
    
    # loop through the difficulties starting from the second-hardest problem
    for i in range(n-2, -1, -1):
        # if the difficulty is greater than twice the maximum difficulty, break the loop
        if a[i] > 2*max_diff:
            break
        # otherwise, increment the number of problems to be included in the contest
        num_problems += 1
    
    return num_problems

def f2(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # initialize the number of problems to be included in the contest
    num_problems = 1
    
    # loop through the difficulties starting from the second-hardest problem
    for i in range(n-2, -1, -1):
        # if the difficulty is greater than twice the maximum difficulty, break the loop
        if a[i] > 2*max_diff:
            break
        # otherwise, increment the number of problems to be included in the contest
        num_problems += 1
    
    return num_problems

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

