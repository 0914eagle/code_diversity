
def count_common_foods(N, M, preferences):
    common_foods = set(preferences[0])
    for i in range(1, N):
        common_foods = common_foods.intersection(set(preferences[i]))
    return len(common_foods)

if __name__ == "__main__":
    N, M = map(int, input().split())
    preferences = [list(map(int, input().split()[1:])) for _ in range(N)]
    result = count_common_foods(N, M, preferences)
    print(result)
