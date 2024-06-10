
def get_valid_scenarios(n, k, x):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over all possible starting positions
    for i in range(1, n+1):
        # Initialize the current position and the number of questions answered
        current_position = i
        questions_answered = 0
        
        # Iterate over all questions
        for j in range(k):
            # If the question is about the current position, answer "NO"
            if x[j] == current_position:
                questions_answered += 1
                continue
            
            # If the question is not about the current position, move to the next cell
            next_position = (current_position + 1) % n + 1
            current_position = next_position
            questions_answered += 1
            
        # If all questions were answered, add the scenario to the set of valid scenarios
        if questions_answered == k:
            valid_scenarios.add((i, current_position))
    
    return len(valid_scenarios)

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(get_valid_scenarios(n, k, x))

if __name__ == '__main__':
    main()

