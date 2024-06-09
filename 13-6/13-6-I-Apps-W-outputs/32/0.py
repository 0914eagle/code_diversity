
def get_min_boxes(n, m, a, X):
    # Initialize a list to store the number of candies in each level
    candies = [0] * (n + 1)
    # Initialize a list to store the number of boxes in each level
    boxes = [0] * (n + 1)
    # Initialize the number of candies in the largest level
    candies[n] = 1
    # Initialize the number of boxes in the largest level
    boxes[n] = a[n]
    
    for i in range(n - 1, -1, -1):
        # Calculate the number of candies in the current level
        candies[i] = candies[i + 1] * boxes[i + 1]
        # Calculate the number of boxes in the current level
        boxes[i] = a[i] * boxes[i + 1] + 1
    
    # Initialize a list to store the minimum number of boxes needed to retrieve X candies
    min_boxes = [0] * m
    
    for i in range(m):
        # Find the level where the required number of candies is available
        for j in range(n, -1, -1):
            if candies[j] >= X[i]:
                break
        # Calculate the minimum number of boxes needed to retrieve X[i] candies
        min_boxes[i] = boxes[j] - 1
    
    return min_boxes

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    X = list(map(int, input().split()))
    min_boxes = get_min_boxes(n, m, a, X)
    for i in range(m):
        print(min_boxes[i])

if __name__ == '__main__':
    main()

