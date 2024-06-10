
import math

def get_min_drill_diameter(flaws):
    # Calculate the center of the flaws
    center = [sum(flaws[:, i]) / len(flaws) for i in range(3)]
    
    # Calculate the distance from the center to each flaw
    dist = [math.sqrt(sum((flaw - center)**2)) for flaw in flaws]
    
    # Return the maximum distance as the minimum drill diameter
    return max(dist) * 2

def main():
    # Read the number of flaws and their positions
    n = int(input())
    flaws = []
    for _ in range(n):
        flaws.append([float(x) for x in input().split()])
    
    # Calculate the minimum drill diameter
    drill_diameter = get_min_drill_diameter(flaws)
    
    # Print the result
    print(drill_diameter)

if __name__ == '__main__':
    main()

