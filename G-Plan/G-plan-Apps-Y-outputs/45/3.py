t_common_foods(N, M, preferences):
    common_foods = set(preferences[0])
    for pref in preferences[1:]:
        common_foods = common_foods.intersection(set(pref))
    return len(common_foods)

if __name__ == "__main__":
    N, M = map(int, input().split())
    preferences = [list(map(int, input().split()[1:])) for _ in range(N)]
    print(count_common_foods(N, M, preferences)