
def get_min_max_area(H, W):
    # Initialize variables
    min_area = float('inf')
    max_area = 0
    
    # Iterate over all possible ways to divide the bar
    for i in range(H):
        for j in range(i+1, H+1):
            for k in range(W):
                for l in range(k+1, W+1):
                    # Calculate the area of each piece
                    area_1 = (j - i) * (l - k)
                    area_2 = (H - j) * (W - l)
                    area_3 = i * k
                    
                    # Update the minimum and maximum areas
                    min_area = min(min_area, min(area_1, area_2, area_3))
                    max_area = max(max_area, max(area_1, area_2, area_3))
    
    # Return the minimum difference between the maximum and minimum areas
    return max_area - min_area

def main():
    # Read the input
    H, W = map(int, input().split())
    
    # Calculate the minimum possible value of S_{max} - S_{min}
    result = get_min_max_area(H, W)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

