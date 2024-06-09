
def get_maximum_ornaments(y, b, r):
    # Initialize variables
    max_ornaments = 0
    yellow_ornaments = 0
    blue_ornaments = 0
    red_ornaments = 0

    # Loop through all possible combinations of ornaments
    for i in range(y):
        for j in range(b):
            for k in range(r):
                # Check if the number of blue ornaments is greater by exactly 1 than the number of yellow ornaments
                if j == i + 1:
                    # Check if the number of red ornaments is greater by exactly 1 than the number of blue ornaments
                    if k == j + 1:
                        # Calculate the total number of ornaments used
                        total_ornaments = i + j + k

                        # Check if the total number of ornaments used is greater than the current maximum
                        if total_ornaments > max_ornaments:
                            # Update the maximum number of ornaments and the corresponding colors of ornaments
                            max_ornaments = total_ornaments
                            yellow_ornaments = i
                            blue_ornaments = j
                            red_ornaments = k

    # Return the maximum number of ornaments and the corresponding colors of ornaments
    return max_ornaments, yellow_ornaments, blue_ornaments, red_ornaments

