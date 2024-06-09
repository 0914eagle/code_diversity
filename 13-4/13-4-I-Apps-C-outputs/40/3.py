
def f1(N, k, heights):
    # Calculate the average height of the houses
    avg_height = sum(heights) / N
    
    # Calculate the new height for each house
    new_heights = [(avg_height + k) if h >= avg_height else h for h in heights]
    
    # Return the new heights
    return new_heights

def f2(N, k, heights):
    # Calculate the final heights of the houses
    final_heights = [f1(N, k, heights)[i] for i in range(N)]
    
    # Return the final height of the tallest house
    return max(final_heights)

if __name__ == '__main__':
    N, k = map(int, input().split())
    heights = list(map(float, input().split()))
    print(f2(N, k, heights))

