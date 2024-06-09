
import math

def get_max_distance(stars):
    # Initialize the maximum distance to 0
    max_distance = 0
    
    # Iterate over the stars
    for star in stars:
        # Calculate the distance that the spaceship can travel from this star
        distance = star[0] - star[1] * math.fabs(math.sin(star[2]))
        
        # Update the maximum distance if necessary
        if distance > max_distance:
            max_distance = distance
    
    # Return the maximum distance
    return max_distance

def main():
    # Read the number of stars
    num_stars = int(input())
    
    # Read the stars
    stars = []
    for _ in range(num_stars):
        stars.append(list(map(float, input().split())))
    
    # Calculate the maximum distance
    max_distance = get_max_distance(stars)
    
    # Print the result
    print(max_distance)

if __name__ == '__main__':
    main()

