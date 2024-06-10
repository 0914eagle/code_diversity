
def get_combinations(candidates, target):
    combinations = []
    for i in range(len(candidates)):
        current_combination = [candidates[i]]
        remaining_candidates = candidates[:i] + candidates[i+1:]
        get_combinations_helper(remaining_candidates, target - candidates[i], current_combination, combinations)
    return combinations

def get_combinations_helper(candidates, target, current_combination, combinations):
    if target == 0:
        combinations.append(current_combination)
        return
    for i in range(len(candidates)):
        if candidates[i] <= target:
            current_combination.append(candidates[i])
            get_combinations_helper(candidates[:i] + candidates[i+1:], target - candidates[i], current_combination, combinations)
            current_combination.pop()

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(get_combinations(candidates, target))

