t_common_foods(N, M, preferences):
    common_foods = set(preferences[0])
    for person in preferences[1:]:
        common_foods = common_foods.intersection(person)
    return len(common_foods)

if __name__ == "__main__":
    N, M = map(int, input().split())
    preferences = []
    for _ in range(N):
        person_prefs = list(map(int, input().split()[1:]))
        preferences.append(set(person_prefs))
    
    result = count_common_foods(N, M, preferences)
    print(result