
def f1(n, heights):
    # Calculate the bitwise OR of all pairs of mountains
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    or_heights = [heights[i] | heights[j] for i, j in pairs]

    # Count the number of pairs with bitwise OR height greater than any mountain height
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if or_heights[i*n + j] > max(heights[i], heights[j]):
                count += 1

    return count

def f2(n, heights):
    # Calculate the bitwise OR of all pairs of mountains
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    or_heights = [heights[i] | heights[j] for i, j in pairs]

    # Find the maximum bitwise OR height
    max_height = max(or_heights)

    # Count the number of pairs with bitwise OR height equal to the maximum height
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if or_heights[i*n + j] == max_height:
                count += 1

    return count

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(f1(n, heights))
    print(f2(n, heights))

