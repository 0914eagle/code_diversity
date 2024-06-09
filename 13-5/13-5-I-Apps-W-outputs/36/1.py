
def f1(n, heights):
    # Calculate the bitwise OR of all pairs of mountains
    bitwise_or = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            bitwise_or[i] |= heights[j - 1]
    
    # Count the number of pairs of mountains with bitwise OR greater than the height of any mountain between them
    count = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if bitwise_or[i] > heights[j - 1]:
                count += 1
    
    return count

def f2(n, heights):
    # Calculate the bitwise OR of all pairs of mountains
    bitwise_or = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            bitwise_or[i] |= heights[j - 1]
    
    # Count the number of pairs of mountains with bitwise OR greater than the height of any mountain between them
    count = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if bitwise_or[i] > heights[j - 1]:
                count += 1
    
    return count

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(f1(n, heights))
    print(f2(n, heights))

