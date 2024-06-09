
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50
    assert 2 <= M <= 50
    dogs = []
    for i in range(N):
        dog = list(map(int, input().split()))
        assert len(dog) == M
        assert all(1 <= t <= 200 for t in dog)
        dogs.append(dog)
    return N, M, dogs

def solve(N, M, dogs):
    # Initialize the waiting time for each dog
    waiting_time = [0] * N

    # Sort the dogs by their eating speed
    dogs.sort(key=lambda x: x[0])

    # Loop through each dog and calculate the waiting time
    for i, dog in enumerate(dogs):
        # Calculate the total waiting time for the current dog
        waiting_time[i] = sum(dog) - dog[0]

    # Return the minimum total waiting time
    return min(waiting_time)

def main():
    N, M, dogs = get_input()
    print(solve(N, M, dogs))

if __name__ == '__main__':
    main()

