
def get_input():
    N, M = map(int, input().split())
    dogs = []
    for i in range(N):
        dogs.append(list(map(int, input().split())))
    return N, M, dogs

def solve(N, M, dogs):
    # Initialize the variables
    feeding_time = [0] * M
    total_time = 0

    # Sort the dogs by their food preferences
    dogs.sort(key=lambda x: x[0])

    # Loop through the dogs and feed them
    for dog in dogs:
        # Find the first empty feeding bowl
        for i in range(M):
            if feeding_time[i] == 0:
                feeding_time[i] = dog[0]
                break

        # Add the feeding time to the total time
        total_time += dog[0]

    return total_time

def main():
    N, M, dogs = get_input()
    print(solve(N, M, dogs))

if __name__ == '__main__':
    main()

