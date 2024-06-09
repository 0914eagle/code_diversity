
def get_absurdity_value(n, k, x):
    # Calculate the total absurdity value for each segment
    total_absurdity = [0] * (n - k + 1)
    for i in range(n):
        total_absurdity[i] += x[i]
        if i + k < n:
            total_absurdity[i + 1] -= x[i]
    
    # Find the maximum total absurdity value
    max_absurdity = max(total_absurdity)
    
    # Find the indices of the segments with the maximum total absurdity value
    indices = [i for i, v in enumerate(total_absurdity) if v == max_absurdity]
    
    return indices

def get_segments(n, k, x):
    # Get the indices of the segments with the maximum total absurdity value
    indices = get_absurdity_value(n, k, x)
    
    # Return the segments with the maximum total absurdity value
    return indices[0], indices[0] + k - 1

if __name__ == '__main__':
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    a, b = get_segments(n, k, x)
    print(a, b)

