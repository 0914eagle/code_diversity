
def get_absurdity_value(n, k, x):
    # Calculate the total absurdity value for each segment
    total_absurdity = [0] * (n - k + 1)
    for i in range(n):
        total_absurdity[i] += x[i]
        if i + k < n:
            total_absurdity[i + 1] -= x[i]
    
    # Find the maximum total absurdity value
    max_absurdity = max(total_absurdity)
    
    # Find the segments with the maximum total absurdity value
    segments = []
    for i in range(n - k + 1):
        if total_absurdity[i] == max_absurdity:
            segments.append(i)
    
    # Return the segments with the maximum total absurdity value
    return segments

def get_optimal_segments(n, k, x):
    # Get the absurdity value for each law
    absurdity = get_absurdity_value(n, k, x)
    
    # Find the optimal segments
    segments = []
    for i in range(n - k + 1):
        for j in range(i + 1, n - k + 2):
            if absurdity[i] + absurdity[j] == max(absurdity):
                segments.append([i, j])
    
    # Return the optimal segments
    return segments

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    segments = get_optimal_segments(n, k, x)
    print(segments[0][0] + 1, segments[0][1] + 1)

if __name__ == '__main__':
    main()

