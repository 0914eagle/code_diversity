
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    food_times = []
    for i in range(N):
        food_times.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for row in food_times for t in row)
    return N, M, food_times

def f1(N, M, food_times):
    # Initialize the solution with the first dog eating from the first bowl
    solution = [0] * N
    solution[0] = 1
    # Initialize the available bowls
    available_bowls = set(range(1, M + 1))
    for i in range(1, N):
        # Find the bowl with the shortest time
        shortest_time = float('inf')
        for j in available_bowls:
            if food_times[i][j] < shortest_time:
                shortest_time = food_times[i][j]
                shortest_bowl = j
        # Assign the dog to eat from the shortest bowl
        solution[i] = shortest_bowl
        # Remove the shortest bowl from the available bowls
        available_bowls.remove(shortest_bowl)
    return solution

def f2(N, M, food_times):
    # Initialize the solution with the first dog eating from the first bowl
    solution = [0] * N
    solution[0] = 1
    # Initialize the available bowls
    available_bowls = set(range(1, M + 1))
    for i in range(1, N):
        # Find the bowl with the shortest time
        shortest_time = float('inf')
        for j in available_bowls:
            if food_times[i][j] < shortest_time:
                shortest_time = food_times[i][j]
                shortest_bowl = j
        # Assign the dog to eat from the shortest bowl
        solution[i] = shortest_bowl
        # Remove the shortest bowl from the available bowls
        available_bowls.remove(shortest_bowl)
    return solution

if __name__ == '__main__':
    N, M, food_times = get_input()
    solution = f1(N, M, food_times)
    print(sum(food_times[i][solution[i] - 1] for i in range(N)))

