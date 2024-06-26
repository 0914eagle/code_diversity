
def find_candidate_locations(robot_image, floor_image):
    # Initialize a list to store the candidate locations
    candidates = []
    
    # Loop through each possible location to overlay the robot image on the floor image
    for x in range(len(floor_image) - len(robot_image) + 1):
        for y in range(len(floor_image[0]) - len(robot_image[0]) + 1):
            # Calculate the number of pixels that are the same between the two images at the current location
            num_same_pixels = 0
            for i in range(len(robot_image)):
                for j in range(len(robot_image[0])):
                    if robot_image[i][j] == floor_image[i + x][j + y]:
                        num_same_pixels += 1
            
            # If the number of same pixels is greater than the current maximum, add the current location to the list of candidates
            if num_same_pixels > max([candidate[2] for candidate in candidates]):
                candidates.append((x, y, num_same_pixels))
    
    # Sort the candidates by x-coordinate and then by y-coordinate
    candidates.sort(key=lambda x: (x[0], x[1]))
    
    # Return the list of candidate locations
    return candidates

