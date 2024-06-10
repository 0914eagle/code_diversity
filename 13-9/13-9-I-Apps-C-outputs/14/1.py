
import math

def get_flaws_diameter(flaws):
    # Calculate the diameter of the largest flaw
    largest_diameter = 0
    for flaw in flaws:
        diameter = 2 * max(abs(flaw[0]), abs(flaw[1]), abs(flaw[2]))
        largest_diameter = max(largest_diameter, diameter)
    
    # Return the diameter of the smallest drill bit that would remove all the flaws
    return largest_diameter

def get_flaws_positions(n):
    # Read the flaws positions from the input
    flaws = []
    for i in range(n):
        flaw = list(map(float, input().split()))
        flaws.append(flaw)
    
    return flaws

def main():
    # Read the number of flaws from the input
    n = int(input())
    
    # Get the positions of the flaws
    flaws = get_flaws_positions(n)
    
    # Calculate the diameter of the smallest drill bit that would remove all the flaws
    diameter = get_flaws_diameter(flaws)
    
    # Print the result
    print(diameter)

if __name__ == '__main__':
    main()

