
def is_possible_triangle(sticks):
    
    # Sort the sticks in descending order
    sticks.sort(reverse=True)

    # Find the longest stick
    longest_stick = sticks[0]

    # Find the second longest stick
    second_longest_stick = sticks[1]

    # Find the shortest stick
    shortest_stick = sticks[2]

    # Calculate the semi-perimeter of the triangle
    semi_perimeter = longest_stick + second_longest_stick + shortest_stick

    # Calculate the area of the triangle
    area = (semi_perimeter - longest_stick) * (semi_perimeter - second_longest_stick) * (semi_perimeter - shortest_stick)

    # Check if the area is positive
    if area > 0:
        return "possible"
    else:
        return "impossible"

