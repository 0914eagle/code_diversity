
def get_amidakuji_count(H, W, K):
    # Initialize a list to store the number of valid amidakuji for each height
    num_amidakuji = [0] * (H + 1)
    num_amidakuji[0] = 1
    
    # Iterate through each height
    for height in range(1, H + 1):
        # Initialize a list to store the number of valid amidakuji that end at each point
        num_valid_amidakuji = [0] * (height + 1)
        num_valid_amidakuji[0] = 1
        
        # Iterate through each point in the current height
        for point in range(1, height + 1):
            # Get the number of valid amidakuji that end at the current point
            num_valid_amidakuji[point] = num_amidakuji[point - 1]
            
            # If the current point is not at the top of the vertical line,
            # add the number of valid amidakuji that end at the previous point
            if point != height:
                num_valid_amidakuji[point] += num_amidakuji[point]
            
        # Update the number of valid amidakuji for the current height
        num_amidakuji[height] = num_valid_amidakuji[height]
    
    # Return the number of valid amidakuji that end at the bottom of the K-th vertical line
    return num_amidakuji[K] % 1000000007

def main():
    H, W, K = map(int, input().split())
    print(get_amidakuji_count(H, W, K))

if __name__ == '__main__':
    main()

