
def f1(N, k, heights):
    # Calculate the average height of the neighbors
    avg_height = sum(heights) / len(heights)
    
    # Calculate the new height for each house
    new_heights = []
    for i in range(N):
        if heights[i] >= avg_height + k:
            new_heights.append(heights[i])
        else:
            new_heights.append((heights[i-1] + heights[i+1]) / 2 + k)
    
    # Return the new heights
    return new_heights

def f2(N, k, heights):
    # Calculate the final heights after infinitely many days
    final_heights = heights
    while True:
        new_heights = f1(N, k, final_heights)
        if new_heights == final_heights:
            break
        final_heights = new_heights
    
    # Return the final height of the tallest house
    return max(final_heights)

if __name__ == '__main__':
    N, k = map(int, input().split())
    heights = list(map(float, input().split()))
    print(f2(N, k, heights))

