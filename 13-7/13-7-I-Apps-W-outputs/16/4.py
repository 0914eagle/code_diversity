
def get_combinations(candidates, target):
    
    combinations = []
    for i in range(len(candidates)):
        current_combination = [candidates[i]]
        remaining_candidates = candidates[:i] + candidates[i+1:]
        for combination in get_combinations(remaining_candidates, target - candidates[i]):
            combinations.append(current_combination + combination)
    if not combinations and target in candidates:
        combinations.append([target])
    return combinations

def get_input():
    
    candidates = list(map(int, input("Enter candidate numbers separated by a space: ").strip().split()))
    target = int(input("Enter target number: "))
    return candidates, target

if __name__ == '__main__':
    candidates, target = get_input()
    combinations = get_combinations(candidates, target)
    print(combinations)

