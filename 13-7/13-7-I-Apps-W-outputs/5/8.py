
def get_message_plan(n, a):
    # Initialize a dictionary to store the message plan
    message_plan = {}
    
    # Iterate through each student and their maximum number of messages
    for i in range(1, n + 1):
        # If the student has at least one message to send
        if a[i - 1] > 0:
            # Add the student to the message plan with their maximum number of messages
            message_plan[i] = a[i - 1]
    
    # Initialize a set to store the students who have already received the message
    received_students = set()
    
    # Initialize a list to store the messages to be sent
    messages = []
    
    # Iterate through each student in the message plan
    for sender in message_plan:
        # Get the maximum number of messages the student can send
        max_messages = message_plan[sender]
        
        # Iterate through each student who has not received the message yet
        for receiver in range(1, n + 1):
            # If the receiver has not received the message yet and the sender can send the message to them
            if receiver not in received_students and sender != receiver:
                # Add the message to the list of messages to be sent
                messages.append((sender, receiver))
                
                # Update the maximum number of messages the sender can send
                max_messages -= 1
                
                # If the sender has sent all their messages, remove them from the message plan
                if max_messages == 0:
                    del message_plan[sender]
                    
                # Add the receiver to the set of students who have received the message
                received_students.add(receiver)
                
                # If all students have received the message, return the list of messages
                if len(received_students) == n:
                    return messages
    
    # If not all students have received the message, return -1
    return -1

def main():
    # Read the number of students and their maximum number of messages from stdin
    n = int(input())
    a = list(map(int, input().split()))
    
    # Get the message plan
    messages = get_message_plan(n, a)
    
    # Print the number of messages to be sent
    print(len(messages))
    
    # Print the messages to be sent, one per line
    for message in messages:
        print(*message)

if __name__ == '__main__':
    main()

