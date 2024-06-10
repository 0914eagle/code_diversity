
def get_candidates(target, candidates):
    return [[candidate] for candidate in candidates if candidate == target]


def get_combinations(target, candidates):
    combinations = []
    for candidate in candidates:
        if candidate > target:
            continue
        combinations.extend([[candidate] + combination for combination in get_combinations(target - candidate, candidates)])
    return combinations


def get_unique_combinations(target, candidates):
    combinations = get_combinations(target, candidates)
    unique_combinations = []
    for combination in combinations:
        if combination not in unique_combinations:
            unique_combinations.append(combination)
    return unique_combinations


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(get_unique_combinations(target, candidates))

