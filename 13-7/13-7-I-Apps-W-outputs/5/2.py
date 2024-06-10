
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_possible_messages(n, a):
    # Initialize the matrix to keep track of the messages
    messages = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the queue with the student number 1
    queue = [1]
    
    # Loop until the queue is empty
    while queue:
        # Get the current student number from the queue
        current_student = queue.pop(0)
        
        # Loop through the students that the current student can send messages to
        for i in range(1, n + 1):
            # Check if the current student can send a message to the student i
            if messages[current_student][i] == 0 and a[current_student] > 0:
                # Update the matrix to keep track of the messages
                messages[current_student][i] = 1
                messages[i][current_student] = 1
                
                # Add the student i to the queue if it hasn't been visited yet
                if i not in queue:
                    queue.append(i)
    
    # Return the matrix of possible messages
    return messages

def get_messages(n, a, messages):
    # Initialize the list of messages
    message_list = []
    
    # Loop through the students
    for i in range(1, n + 1):
        # Loop through the students that the current student can send messages to
        for j in range(1, n + 1):
            # Check if the current student can send a message to the student j
            if messages[i][j] == 1:
                # Add the message to the list
                message_list.append((i, j))
    
    # Return the list of messages
    return message_list

def get_output(n, a, message_list):
    # Print the number of messages
    print(len(message_list))
    
    # Loop through the messages
    for message in message_list:
        # Print the message
        print(message[0], message[1])

def main():
    # Get the input
    n, a = get_input()
    
    # Get the possible messages
    messages = get_possible_messages(n, a)
    
    # Get the list of messages
    message_list = get_messages(n, a, messages)
    
    # Get the output
    get_output(n, a, message_list)

if __name__ == '__main__':
    main()

