
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    food_preferences = []
    for _ in range(N):
        food_preferences.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for row in food_preferences for t in row)
    return N, M, food_preferences

def solve(N, M, food_preferences):
    # Initialize a list to store the minimum time required to feed each dog
    min_times = [0] * N
    # Loop through each dog
    for i in range(N):
        # Loop through each bowl
        for j in range(M):
            # If the current time required to feed the dog is greater than the minimum time required to feed the dog
            if min_times[i] < food_preferences[i][j]:
                # Update the minimum time required to feed the dog
                min_times[i] = food_preferences[i][j]
    # Return the sum of the minimum times required to feed all dogs
    return sum(min_times)

def main():
    N, M, food_preferences = get_input()
    print(solve(N, M, food_preferences))

if __name__ == '__main__':
    main()

