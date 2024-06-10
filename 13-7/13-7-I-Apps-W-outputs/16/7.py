
def get_candidates(candidates, target):
    # create a list to store the combinations
    combinations = []
    
    # loop through each candidate and check if it is equal to the target
    for candidate in candidates:
        if candidate == target:
            # if the candidate is equal to the target, add it to the combinations list
            combinations.append([candidate])
    
    # return the combinations list
    return combinations

def get_combinations(candidates, target):
    # create a list to store the combinations
    combinations = []
    
    # loop through each candidate and check if it is less than the target
    for candidate in candidates:
        if candidate < target:
            # if the candidate is less than the target, get the combinations for the remaining candidates and the target minus the candidate
            remaining_combinations = get_combinations(candidates, target - candidate)
            
            # loop through each combination and add the candidate to it
            for combination in remaining_combinations:
                combination.append(candidate)
                
            # add the combinations to the combinations list
            combinations += remaining_combinations
    
    # return the combinations list
    return combinations

def main():
    # test get_candidates function
    print("Test get_candidates function:")
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    combinations = get_candidates(candidates, target)
    print(combinations)
    
    # test get_combinations function
    print("Test get_combinations function:")
    candidates = [2, 5, 2, 1, 2]
    target = 5
    combinations = get_combinations(candidates, target)
    print(combinations)

if __name__ == '__main__':
    main()

