
def solve(n, answers):
    # Initialize variables to keep track of the correct answers for each boy
    adrian_correct = 0
    bruno_correct = 0
    goran_correct = 0
    
    # Iterate through the answers and count the correct answers for each boy
    for i, answer in enumerate(answers):
        if i % 3 == 0:
            # Adrian's sequence
            if answer == "A":
                adrian_correct += 1
            elif answer == "B":
                bruno_correct += 1
            else:
                goran_correct += 1
        elif i % 3 == 1:
            # Bruno's sequence
            if answer == "B":
                bruno_correct += 1
            elif answer == "A":
                adrian_correct += 1
            else:
                goran_correct += 1
        else:
            # Goran's sequence
            if answer == "C":
                goran_correct += 1
            elif answer == "A":
                adrian_correct += 1
            else:
                bruno_correct += 1
    
    # Find the maximum number of correct answers among the three boys
    max_correct = max(adrian_correct, bruno_correct, goran_correct)
    
    # Print the names of the boys whose sequences result in the maximum number of correct answers
    if adrian_correct == max_correct:
        print("Adrian")
    if bruno_correct == max_correct:
        print("Bruno")
    if goran_correct == max_correct:
        print("Goran")

