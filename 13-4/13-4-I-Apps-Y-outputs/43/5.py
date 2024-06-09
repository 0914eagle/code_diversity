
def get_min_distance(num_balls, robot_positions, ball_positions):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    
    # Loop through each robot position
    for robot_position in robot_positions:
        # Get the distance from the robot to the ball
        distance = abs(robot_position - ball_positions[0])
        
        # If the distance is less than the minimum distance, update the minimum distance
        if distance < min_distance:
            min_distance = distance
    
    # Return the minimum distance
    return min_distance

def main():
    # Read the input data
    num_balls, robot_positions, ball_positions = read_input()
    
    # Get the minimum distance
    min_distance = get_min_distance(num_balls, robot_positions, ball_positions)
    
    # Print the minimum distance
    print(min_distance)

def read_input():
    # Read the number of balls
    num_balls = int(input())
    
    # Read the robot positions
    robot_positions = [int(x) for x in input().split()]
    
    # Read the ball positions
    ball_positions = [int(x) for x in input().split()]
    
    # Return the input data
    return num_balls, robot_positions, ball_positions

if __name__ == '__main__':
    main()

