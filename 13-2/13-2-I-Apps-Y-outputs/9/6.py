
def get_cleanup_phases(n, dirty_pushes):
    # Initialize variables
    cleanup_phases = 0
    dirtiness = 0

    # Iterate through the dirty pushes
    for i in range(n):
        # Calculate the dirtiness for the current day
        dirtiness += dirty_pushes[i]

        # Check if the dirtiness is greater than or equal to 20
        if dirtiness >= 20:
            # Increment the cleanup phases
            cleanup_phases += 1

            # Reset the dirtiness to 0
            dirtiness = 0

    return cleanup_phases

if __name__ == '__main__':
    n = int(input())
    dirty_pushes = list(map(int, input().split()))
    print(get_cleanup_phases(n, dirty_pushes))

