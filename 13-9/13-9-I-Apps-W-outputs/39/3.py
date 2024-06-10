
def get_scenarios(n, k, questions):
    # Initialize a set to store the valid scenarios
    scenarios = set()
    
    # Iterate over each question
    for i in range(k):
        # Get the current and next questions
        current_question = questions[i]
        next_question = questions[(i + 1) % k]
        
        # Check if the current question is adjacent to the next question
        if current_question + 1 == next_question or current_question - 1 == next_question:
            # If they are adjacent, add the current question to the set of valid scenarios
            scenarios.add(current_question)
    
    # Return the number of valid scenarios
    return len(scenarios)

def main():
    # Read the input data
    n, k = map(int, input().strip().split())
    questions = tuple(map(int, input().strip().split()))
    
    # Call the get_scenarios function and print the result
    result = get_scenarios(n, k, questions)
    print(result)

if __name__ == '__main__':
    main()

