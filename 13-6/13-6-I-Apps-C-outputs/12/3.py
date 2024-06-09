
def get_max_distance(stars):
    # Sort the stars by their angle with the x-axis in ascending order
    stars.sort(key=lambda x: x[2])
    
    # Initialize the maximum distance traveled
    max_distance = 0
    
    # Iterate over the stars
    for i in range(len(stars)):
        # Calculate the distance traveled by the current star
        distance = stars[i][0] - stars[i][1] * abs(stars[i][2] - stars[i-1][2]) if i > 0 else stars[i][0]
        
        # Update the maximum distance traveled
        max_distance = max(max_distance, distance)
    
    return max_distance

def main():
    # Read the number of stars
    num_stars = int(input())
    
    # Read the information of each star
    stars = []
    for _ in range(num_stars):
        t, s, a = map(float, input().split())
        stars.append((t, s, a))
    
    # Find the maximum distance traveled
    max_distance = get_max_distance(stars)
    
    # Print the result
    print(max_distance)

if __name__ == '__main__':
    main()

