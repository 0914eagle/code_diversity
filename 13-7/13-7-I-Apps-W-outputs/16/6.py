
def get_candidates(candidates, target):
    return candidates

def get_combinations(candidates, target):
    combinations = []
    for candidate in candidates:
        if candidate == target:
            combinations.append([candidate])
        elif candidate < target:
            for combination in get_combinations(candidates, target - candidate):
                combinations.append([candidate] + combination)
    return combinations

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(get_combinations(candidates, target))

if __name__ == '__main__':
    main()

