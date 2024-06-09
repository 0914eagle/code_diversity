
def get_max_standers(n, people):
    # Initialize a list to store the answers
    answers = []
    
    # Loop through each possible combination of standers
    for combination in itertools.permutations(range(1, n + 1)):
        # Check if the current combination is valid
        if is_valid_combination(combination, people):
            # If it is valid, add it to the list of answers
            answers.append(combination)
    
    # Return the list of answers
    return answers

def is_valid_combination(combination, people):
    # Initialize a set to store the standers on each button
    standers = set()
    
    # Loop through each person in the combination
    for person in combination:
        # Check if the person is standing on a button that is already occupied
        if person in standers:
            # If they are, return False
            return False
        # Add the person to the set of standers on the button
        standers.add(person)
    
    # If we reach this point, all standers are unique, so return True
    return True

def main():
    # Read the input from stdin
    n = int(input())
    people = []
    for i in range(n):
        line = input()
        people.append(line)
    
    # Call the function to get the maximum number of standers
    answers = get_max_standers(n, people)
    
    # Print the number of answers
    print(len(answers))
    
    # Loop through each answer and print it
    for answer in answers:
        print(*answer)

if __name__ == "__main__":
    main()

