
def get_messages(n, a):
    # Initialize a dictionary to store the messages
    messages = {}
    
    # Initialize a queue to store the students to send messages to
    queue = [1]
    
    # Loop through the students to send messages
    while queue:
        # Get the current student from the queue
        current_student = queue.pop(0)
        
        # Loop through the students who can receive messages
        for i in range(1, n + 1):
            # Check if the student has not already sent a message
            if i not in messages:
                # Check if the student is not the current student
                if i != current_student:
                    # Check if the student has not exceeded the maximum number of messages
                    if a[i] > 0:
                        # Send a message from the current student to the student
                        messages[i] = current_student
                        a[i] -= 1
                        
                        # Add the student to the queue
                        queue.append(i)
    
    # Return the messages
    return messages

def print_messages(messages):
    # Initialize a list to store the printed messages
    printed_messages = []
    
    # Loop through the messages
    for student, sender in messages.items():
        # Check if the student has not already received a message
        if student not in printed_messages:
            # Print the message
            printed_messages.append(student)
            print(sender, student)
    
    # Return the printed messages
    return printed_messages

if __name__ == '__main__':
    # Get the number of students
    n = int(input())
    
    # Get the maximum number of messages for each student
    a = list(map(int, input().split()))
    
    # Get the messages
    messages = get_messages(n, a)
    
    # Print the messages
    print_messages(messages)

