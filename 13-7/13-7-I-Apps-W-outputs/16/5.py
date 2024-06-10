
def find_combinations(candidates, target):
    # Sort the candidates in ascending order
    candidates.sort()
    # Initialize an empty list to store the combinations
    combinations = []
    # Loop through each candidate and try to find combinations that sum to the target
    for i in range(len(candidates)):
        current_candidate = candidates[i]
        if current_candidate > target:
            # If the current candidate is greater than the target, we can't find any combinations with it
            break
        # Find the combinations for the remaining candidates that sum to the target minus the current candidate
        remaining_combinations = find_combinations(candidates[i+1:], target - current_candidate)
        # Add the current candidate to each of the combinations for the remaining candidates
        for combination in remaining_combinations:
            combination.append(current_candidate)
        # Add the combinations for the remaining candidates to the list of combinations
        combinations += remaining_combinations
    return combinations

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    combinations = find_combinations(candidates, target)
    print(combinations)

if __name__ == '__main__':
    main()

