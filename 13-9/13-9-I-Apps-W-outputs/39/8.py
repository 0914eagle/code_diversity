
def get_valid_scenarios(n, k, questions):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over all possible starting positions
    for i in range(1, n + 1):
        # Initialize the current position and the number of questions answered
        current_position = i
        num_questions_answered = 0
        
        # Iterate over the questions
        for j in range(k):
            # If the current position is the question, answer "NO" and move to the next position
            if current_position == questions[j]:
                num_questions_answered += 1
                current_position += 1
                
                # If the current position is out of bounds, move back to the starting position
                if current_position > n:
                    current_position = i
            
        # If all questions were answered "NO", add the scenario to the set of valid scenarios
        if num_questions_answered == k:
            valid_scenarios.add((i, current_position))
    
    return len(valid_scenarios)

def main():
    n, k = map(int, input().split())
    questions = list(map(int, input().split()))
    print(get_valid_scenarios(n, k, questions))

if __name__ == '__main__':
    main()

