
def determine_wizard_number(N, K):
    # Initialize a list to store the questions
    questions = []
    
    # Question 1: Is the number even?
    questions.append(lambda x: x % 2 == 0)
    
    # Question 2: Is the number between 7 and 10 (inclusive)?
    questions.append(lambda x: 7 <= x <= 10)
    
    # Question 3: Is the number prime?
    questions.append(lambda x: is_prime(x))
    
    # Ask the questions and get the answers from the Wizard
    answers = []
    for question in questions:
        answers.append(question(N))
    
    # Use the answers to determine the Wizard's secret number
    secret_number = 1
    for i in range(K):
        if answers[i]:
            secret_number = 2 * secret_number
        secret_number += 1
    
    return secret_number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N, K = map(int, input().split())
    if determine_wizard_number(N, K) == N:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")

if __name__ == '__main__':
    main()

