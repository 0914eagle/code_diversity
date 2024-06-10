
def get_throws(target_score):
    # Initialize a list to store the throw scores
    throws = []
    
    # Iterate through the sections of the dartboard (1 to 20)
    for section in range(1, 20 + 1):
        # If the target score is less than or equal to the section score, add a single throw to the list
        if target_score <= section:
            throws.append(f"single {section}")
            target_score -= section
    
    # If the target score is still positive, iterate through the sections again and add double and triple throws as needed
    if target_score > 0:
        for section in range(1, 20 + 1):
            # If the target score is less than or equal to the double section score, add a double throw to the list
            if target_score <= 2 * section:
                throws.append(f"double {section}")
                target_score -= 2 * section
            
            # If the target score is less than or equal to the triple section score, add a triple throw to the list
            if target_score <= 3 * section:
                throws.append(f"triple {section}")
                target_score -= 3 * section
    
    # If the target score is still positive, it is impossible to achieve the target score with three throws
    if target_score > 0:
        return "impossible"
    
    # Return the list of throws
    return throws

def main():
    # Read the target score from stdin
    target_score = int(input())
    
    # Call the get_throws function and print the output
    print("\n".join(get_throws(target_score)))

if __name__ == '__main__':
    main()

