
def get_correct_answers(exam_answers):
    # Initialize a dictionary to store the number of correct answers for each boy
    correct_answers = {"Adrian": 0, "Bruno": 0, "Goran": 0}
    
    # Iterate through the exam answers
    for i, answer in enumerate(exam_answers):
        # Get the current boy's sequence
        if i % 3 == 0:
            current_boy = "Adrian"
        elif i % 3 == 1:
            current_boy = "Bruno"
        else:
            current_boy = "Goran"
        
        # Check if the current answer is correct
        if answer == "A":
            correct_answers[current_boy] += 1
        elif answer == "B":
            if current_boy == "Bruno":
                correct_answers[current_boy] += 1
        elif answer == "C":
            if current_boy == "Goran":
                correct_answers[current_boy] += 1
    
    # Return the boy with the most correct answers
    return max(correct_answers, key=correct_answers.get)

def main():
    # Read the exam answers from stdin
    exam_answers = input()
    
    # Get the correct answers for each boy
    correct_answers = get_correct_answers(exam_answers)
    
    # Print the result
    print(correct_answers)

if __name__ == '__main__':
    main()

