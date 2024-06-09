
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def get_min_abs_diff(a, b):
    # Calculate the absolute difference between the sums of a and b
    abs_diff = abs(sum(a) - sum(b))
    
    # If the absolute difference is 0, return the empty string
    if abs_diff == 0:
        return ""
    
    # Otherwise, find the indices of the elements in a and b that have the smallest absolute difference
    min_abs_diff_indices = [i for i, x in enumerate(a) if abs(x - b[i]) == abs_diff]
    
    # If there is only one index with the smallest absolute difference, return the corresponding character
    if len(min_abs_diff_indices) == 1:
        return "A" if a[min_abs_diff_indices[0]] > b[min_abs_diff_indices[0]] else "B"
    
    # Otherwise, find the lexicographically smallest solution
    min_solution = ""
    for i in min_abs_diff_indices:
        if a[i] > b[i]:
            min_solution += "A"
        else:
            min_solution += "B"
    
    return min_solution

def solve(N, a, b):
    return get_min_abs_diff(a, b)

if __name__ == '__main__':
    N, a, b = get_input()
    print(solve(N, a, b))

