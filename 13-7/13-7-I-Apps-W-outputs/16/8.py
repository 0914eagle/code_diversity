
def find_combinations(candidates, target):
    combinations = []
    for i in range(len(candidates)):
        current_combination = [candidates[i]]
        current_sum = candidates[i]
        for j in range(i+1, len(candidates)):
            if current_sum + candidates[j] == target:
                current_combination.append(candidates[j])
                combinations.append(current_combination)
                break
            elif current_sum + candidates[j] < target:
                current_combination.append(candidates[j])
                current_sum += candidates[j]
    return combinations

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    combinations = find_combinations(candidates, target)
    print(combinations)

if __name__ == '__main__':
    main()

