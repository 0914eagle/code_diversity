
def get_minimum_boxes(n, m, a, X):
    # Calculate the total number of candies in each box
    total_candies = [0] * (n + 1)
    total_candies[0] = 1
    for i in range(1, n + 1):
        total_candies[i] = total_candies[i - 1] * a[i - 1]
    
    # Initialize the minimum number of boxes to open
    min_boxes = [0] * m
    
    # Loop through each query
    for i in range(m):
        # Find the box that contains the required number of candies
        for j in range(n, -1, -1):
            if total_candies[j] >= X[i]:
                min_boxes[i] = j
                break
    
    return min_boxes

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    X = list(map(int, input().split()))
    min_boxes = get_minimum_boxes(n, m, a, X)
    for i in range(m):
        print(min_boxes[i])

if __name__ == '__main__':
    main()

