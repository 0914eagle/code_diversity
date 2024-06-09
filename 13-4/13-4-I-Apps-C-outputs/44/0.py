
def get_max_people_on_buttons(n, buttons):
    # Initialize a list to store the people standing on each button
    people_on_buttons = [[] for _ in range(n)]
    
    # Initialize a set to store the people who have not been placed on a button yet
    unplaced_people = set(range(n))
    
    # Initialize a variable to store the maximum number of people on buttons
    max_people_on_buttons = 0
    
    # Loop until all people have been placed on buttons
    while unplaced_people:
        # Get the next person to be placed on a button
        person = unplaced_people.pop()
        
        # Loop through the buttons to find an available button
        for button in range(n):
            if button not in people_on_buttons[button]:
                # Place the person on the button
                people_on_buttons[button].append(person)
                
                # Remove the person from the set of unplaced people
                unplaced_people.remove(person)
                
                # Increment the maximum number of people on buttons
                max_people_on_buttons += 1
                
                # Break out of the loop once the person has been placed
                break
    
    # Return the maximum number of people on buttons and the people standing on each button
    return max_people_on_buttons, people_on_buttons

