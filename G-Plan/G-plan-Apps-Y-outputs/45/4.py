
def count_common_foods(N, M, preferences):
    common_foods = set(preferences[0])
    for pref in preferences[1:]:
        common_foods = common_foods.intersection(pref)
    return len(common_foods)

if __name__ == "__main__":
    N, M = map(int, input().split())
    preferences = []
    for _ in range(N):
        pref = list(map(int, input().split()))[1:]
        preferences.append(set(pref))
    print(count_common_foods(N, M, preferences))