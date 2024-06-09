
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    food_times = []
    for _ in range(N):
        food_times.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for t in food_times)
    return N, M, food_times

def f1(N, M, food_times):
    # initialize the variables
    max_time = 0
    min_time = 0
    dog_count = [0] * M
    bowl_count = [0] * M
    for i in range(N):
        for j in range(M):
            if food_times[i][j] > max_time:
                max_time = food_times[i][j]
            if food_times[i][j] < min_time:
                min_time = food_times[i][j]
            dog_count[j] += 1
            bowl_count[j] += food_times[i][j]
    
    # calculate the total waiting time
    total_time = 0
    for i in range(M):
        total_time += (dog_count[i] - 1) * min_time
    
    return total_time

def f2(N, M, food_times):
    # sort the food times in ascending order
    sorted_food_times = sorted(food_times, key=lambda x: x[0])
    
    # initialize the variables
    max_time = 0
    min_time = 0
    dog_count = [0] * M
    bowl_count = [0] * M
    for i in range(N):
        for j in range(M):
            if sorted_food_times[i][j] > max_time:
                max_time = sorted_food_times[i][j]
            if sorted_food_times[i][j] < min_time:
                min_time = sorted_food_times[i][j]
            dog_count[j] += 1
            bowl_count[j] += sorted_food_times[i][j]
    
    # calculate the total waiting time
    total_time = 0
    for i in range(M):
        total_time += (dog_count[i] - 1) * min_time
    
    return total_time

if __name__ == '__main__':
    N, M, food_times = get_input()
    print(f1(N, M, food_times))
    print(f2(N, M, food_times))

