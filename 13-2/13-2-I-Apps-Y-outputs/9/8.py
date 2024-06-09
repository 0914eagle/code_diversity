
def get_cleanup_phases(n, dirty_pushes):
    # Initialize variables
    cleanup_phases = 0
    dirtiness = 0

    # Sort the dirty pushes in ascending order
    dirty_pushes.sort()

    # Loop through each dirty push and calculate the dirtiness
    for i in range(n):
        dirtiness += dirty_pushes[i]
        if dirtiness > 20:
            cleanup_phases += 1
            dirtiness = 0

    return cleanup_phases

def main():
    n = int(input())
    dirty_pushes = list(map(int, input().split()))
    print(get_cleanup_phases(n, dirty_pushes))

if __name__ == '__main__':
    main()

