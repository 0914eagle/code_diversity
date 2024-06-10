
def get_candidates(target, candidates):
    return [(candidates[i], target-candidates[i]) for i in range(len(candidates)) if candidates[i] <= target]

def get_combinations(candidates, target, combinations=[]):
    if not candidates:
        return combinations
    combination = candidates[0]
    combinations = get_combinations(candidates[1:], target-combination, combinations + [combination])
    return get_combinations(candidates[1:], target, combinations)

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(get_combinations(candidates, target))

if __name__ == '__main__':
    main()

