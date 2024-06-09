
def f1(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # find the index of the maximum difficulty
    max_index = a.index(max_diff)
    
    # initialize the number of problems to be included in the contest as the maximum index
    num_problems = max_index
    
    # loop through the difficulties in reverse order
    for i in range(max_index - 1, -1, -1):
        # if the current difficulty is greater than twice the previous difficulty, include it in the contest
        if a[i] > a[i + 1] * 2:
            num_problems += 1
    
    return num_problems

def f2(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # find the index of the maximum difficulty
    max_index = a.index(max_diff)
    
    # initialize the number of problems to be included in the contest as the maximum index
    num_problems = max_index
    
    # loop through the difficulties in reverse order
    for i in range(max_index - 1, -1, -1):
        # if the current difficulty is greater than twice the previous difficulty, include it in the contest
        if a[i] > a[i + 1] * 2:
            num_problems += 1
    
    return num_problems

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

