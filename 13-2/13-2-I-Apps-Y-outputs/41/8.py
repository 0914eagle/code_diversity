
def safe_order(n, students):
    # Initialize the pile with the first room's exams
    pile = sum(students)
    # Initialize the safe order with the first room
    order = [1]
    # Loop through the remaining rooms
    for i in range(2, n+1):
        # If the pile has enough exams, distribute them randomly to the students in the current room
        if pile >= students[i-1]:
            pile -= students[i-1]
            order.append(i)
        # If the pile runs out of exams, return "impossible"
        else:
            return "impossible"
    # Return the safe order
    return order

