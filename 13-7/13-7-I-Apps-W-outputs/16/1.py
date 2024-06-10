
def find_combinations(candidates, target):
    # Sort the candidates in ascending order
    candidates.sort()
    # Initialize an empty list to store the combinations
    combinations = []
    # Iterate over the candidates and try to find combinations that sum to the target
    for i in range(len(candidates)):
        current_combination = [candidates[i]]
        current_sum = candidates[i]
        for j in range(i+1, len(candidates)):
            current_sum += candidates[j]
            if current_sum == target:
                current_combination.append(candidates[j])
                combinations.append(current_combination)
                break
            elif current_sum > target:
                break
    return combinations

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    combinations = find_combinations(candidates, target)
    print(combinations)

if __name__ == '__main__':
    main()

