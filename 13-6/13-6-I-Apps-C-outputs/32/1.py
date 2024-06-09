
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    food_bowls = []
    for _ in range(N):
        food_bowls.append(list(map(int, input().split())))
    return N, M, food_bowls

def f1(N, M, food_bowls):
    # Initialize the waiting times for each dog
    waiting_times = [0] * N

    # Sort the food bowls by the amount of time each dog will spend eating
    sorted_food_bowls = sorted(food_bowls, key=lambda x: x[0])

    # Loop through each dog and assign them to a food bowl
    for i in range(N):
        waiting_times[i] += sorted_food_bowls[i][0]
        sorted_food_bowls[i][0] = 0

    # Loop through each dog and assign them to the next available food bowl
    for i in range(N):
        for j in range(M):
            if sorted_food_bowls[i][j] > 0:
                waiting_times[i] += sorted_food_bowls[i][j]
                sorted_food_bowls[i][j] = 0
                break

    return waiting_times

def f2(N, M, food_bowls):
    # Initialize the waiting times for each dog
    waiting_times = [0] * N

    # Sort the food bowls by the amount of time each dog will spend eating
    sorted_food_bowls = sorted(food_bowls, key=lambda x: x[0])

    # Loop through each dog and assign them to a food bowl
    for i in range(N):
        waiting_times[i] += sorted_food_bowls[i][0]
        sorted_food_bowls[i][0] = 0

    # Loop through each dog and assign them to the next available food bowl
    for i in range(N):
        for j in range(M):
            if sorted_food_bowls[i][j] > 0:
                waiting_times[i] += sorted_food_bowls[i][j]
                sorted_food_bowls[i][j] = 0
                break

    return waiting_times

def main():
    N, M, food_bowls = get_input()
    waiting_times = f1(N, M, food_bowls)
    print(sum(waiting_times))

if __name__ == '__main__':
    main()

