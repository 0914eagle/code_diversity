
def count_common_foods(N, M, preferences):
    common_foods = set(preferences[0])
    for person_prefs in preferences[1:]:
        common_foods = common_foods.intersection(person_prefs)
    return len(common_foods)

if __name__ == "__main__":
    N, M = map(int, input().split())
    preferences = []
    for _ in range(N):
        prefs = list(map(int, input().split()))[1:]
        preferences.append(set(prefs))
    
    result = count_common_foods(N, M, preferences)
    print(result)
