
def get_min_boxes(n, m, a, X):
    # Initialize a list to store the number of candies in each box
    candies = [0] * (n + 1)
    candies[0] = 1
    
    # Calculate the number of candies in each box
    for i in range(1, n + 1):
        candies[i] = candies[i - 1] * a[i - 1]
    
    # Initialize a list to store the minimum number of boxes needed to retrieve X candies
    min_boxes = [0] * m
    
    # Loop through each query
    for i in range(m):
        # Find the box that contains at least X[i] candies
        for j in range(n, -1, -1):
            if candies[j] >= X[i]:
                min_boxes[i] = j
                break
    
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

