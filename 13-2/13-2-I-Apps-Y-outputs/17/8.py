
def is_possible(buttons):
    # Initialize variables
    current_button = 1
    visited_buttons = set()
    count = 0

    # Loop through the buttons
    while current_button != 2:
        # If we have visited this button before, return False
        if current_button in visited_buttons:
            return -1

        # Add the current button to the visited buttons
        visited_buttons.add(current_button)

        # Get the next button to press
        next_button = buttons[current_button - 1]

        # Update the current button and count
        current_button = next_button
        count += 1

    # If we reach here, it means we have found a way to lighten up Button 2
    return count

