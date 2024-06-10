
def determine_secret_number(N, K):
    # Initialize a list to store the questions
    questions = []
    
    # Question 1: Is the number even?
    questions.append("Is the number even?")
    
    # Question 2: Is the number between 7 and 10 (inclusive)?
    questions.append("Is the number between 7 and 10?")
    
    # Question 3: Is the number prime?
    questions.append("Is the number prime?")
    
    # Ask the questions and get the answers from the Wizard
    answers = []
    for question in questions:
        answer = input(question + " (y/n): ")
        answers.append(answer)
    
    # Process the answers to determine the secret number
    secret_number = 1
    for i in range(K):
        if answers[i] == "y":
            secret_number *= 2
        else:
            secret_number *= 3
            if i == 0:
                secret_number += 1
    
    return secret_number

def main():
    N, K = map(int, input().split())
    secret_number = determine_secret_number(N, K)
    print(f"Your wish is granted! The secret number is {secret_number}.")

if __name__ == '__main__':
    main()

