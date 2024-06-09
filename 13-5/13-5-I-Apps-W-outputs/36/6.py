
def f1(n, heights):
    # Calculate the bitwise OR of all pairs of mountains
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    or_values = [heights[i] | heights[j] for i, j in pairs]

    # Count the number of pairs where the bitwise OR is greater than the height of any mountain in the range
    count = 0
    for i, j in pairs:
        if or_values[i] > max(heights[k] for k in range(i, j+1)):
            count += 1

    return count

def f2(n, heights):
    # Calculate the bitwise OR of all subarrays of mountains
    subarrays = [heights[i:j+1] for i in range(n) for j in range(i, n)]
    or_values = [sum(subarray) for subarray in subarrays]

    # Count the number of subarrays where the bitwise OR is greater than the height of any mountain in the subarray
    count = 0
    for subarray in subarrays:
        if sum(subarray) > max(subarray):
            count += 1

    return count

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(f1(n, heights))
    print(f2(n, heights))

