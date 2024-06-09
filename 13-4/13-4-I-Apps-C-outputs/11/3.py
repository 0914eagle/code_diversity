
import math

def get_input():
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_max_sliced_fruits(n, fruits):
    # Find the minimum and maximum x-coordinates of all fruits
    min_x = min(fruit[0] for fruit in fruits)
    max_x = max(fruit[0] for fruit in fruits)
    
    # Find the minimum and maximum y-coordinates of all fruits
    min_y = min(fruit[1] for fruit in fruits)
    max_y = max(fruit[1] for fruit in fruits)
    
    # Calculate the slope and y-intercept of the line that passes through the minimum and maximum points
    slope = (max_y - min_y) / (max_x - min_x)
    y_intercept = min_y - slope * min_x
    
    # Initialize the maximum number of sliced fruits to 0
    max_sliced_fruits = 0
    
    # Loop through all fruits and check if they are intersected by the line
    for fruit in fruits:
        # Calculate the distance from the fruit to the line
        distance = abs(slope * fruit[0] - fruit[1] + y_intercept) / math.sqrt(slope ** 2 + 1)
        
        # If the distance is less than or equal to the radius of the fruit, the fruit is intersected
        if distance <= 1:
            max_sliced_fruits += 1
    
    return max_sliced_fruits

def main():
    n, fruits = get_input()
    print(get_max_sliced_fruits(n, fruits))

if __name__ == '__main__':
    main()

