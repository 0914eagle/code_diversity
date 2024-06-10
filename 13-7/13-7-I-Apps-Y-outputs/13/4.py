
def determine_wizard_secret(N, K):
    # Initialize a set to store the possible numbers
    possible_numbers = set(range(1, N+1))
    
    # Iterate over the questions
    for _ in range(K):
        # Ask the question
        question = input("Enter a question (e.g. 'Is the number even?'): ")
        
        # Get the answer
        answer = input("Enter the answer (e.g. 'true' or 'false'): ")
        
        # Update the possible numbers based on the question and answer
        if answer == "true":
            possible_numbers = set(filter(lambda x: eval(question), possible_numbers))
        else:
            possible_numbers = set(filter(lambda x: not eval(question), possible_numbers))
    
    # If there is only one possible number, return it
    if len(possible_numbers) == 1:
        return possible_numbers.pop()
    # Otherwise, return -1
    else:
        return -1

def main():
    N, K = map(int, input().split())
    secret_number = determine_wizard_secret(N, K)
    if secret_number == -1:
        print("You will become a flying monkey!")
    else:
        print("Your wish is granted!")

if __name__ == '__main__':
    main()

