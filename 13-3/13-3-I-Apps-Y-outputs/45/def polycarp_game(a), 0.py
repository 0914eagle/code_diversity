
def polycarp_game(a):
    # Initialize the sum of non-deleted elements
    sum_of_non_deleted_elements = sum(a)
    # Initialize the number of moves
    number_of_moves = 0
    # Initialize the parity of the last deleted element
    last_deleted_element_parity = None

    while a:
        # If it is the first move, choose any element and delete it
        if number_of_moves == 0:
            element_to_delete = a.pop()
        # If it is the second or any next move:
        else:
            # If the last deleted element was odd, choose any even element and delete it
            if last_deleted_element_parity == "odd":
                element_to_delete = a[0]
                a.pop(0)
            # If the last deleted element was even, choose any odd element and delete it
            else:
                element_to_delete = a[-1]
                a.pop()
        # Update the sum of non-deleted elements
        sum_of_non_deleted_elements -= element_to_delete
        # Update the number of moves
        number_of_moves += 1
        # Update the parity of the last deleted element
        last_deleted_element_parity = "odd" if element_to_delete % 2 == 1 else "even"

    return sum_of_non_deleted_elements

