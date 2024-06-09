
def get_cleanup_phases(days):
    # Initialize variables
    cleanup_phases = 0
    dirtiness = 0

    # Iterate through the days
    for i in range(len(days)):
        # Calculate the dirtiness for the current day
        dirtiness += days[i]

        # Check if the dirtiness is greater than or equal to 20
        if dirtiness >= 20:
            # Increment the cleanup phases
            cleanup_phases += 1

            # Reset the dirtiness to 0
            dirtiness = 0

    return cleanup_phases

if __name__ == '__main__':
    days = [1, 45, 65, 84, 346]
    print(get_cleanup_phases(days))

