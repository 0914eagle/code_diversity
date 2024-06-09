
def get_cleanup_phases(dirty_pushes):
    # Initialize variables
    cleanup_phases = 0
    dirtiness = 0

    # Iterate through the dirty pushes
    for i in range(len(dirty_pushes)):
        # Calculate the dirtiness for the current day
        dirtiness += dirty_pushes[i]

        # Check if the dirtiness exceeds 20
        if dirtiness > 20:
            # Increment the cleanup phases
            cleanup_phases += 1

            # Reset the dirtiness to the current dirty push
            dirtiness = dirty_pushes[i]

    return cleanup_phases

if __name__ == '__main__':
    dirty_pushes = [1, 45, 65, 84, 346]
    print(get_cleanup_phases(dirty_pushes))

