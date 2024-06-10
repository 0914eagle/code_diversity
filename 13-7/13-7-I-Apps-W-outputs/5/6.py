
def get_plan(n, a):
    # Initialize a graph to represent the relationships between students
    graph = [[] for _ in range(n + 1)]
    
    # Add edges to the graph based on the values of a
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and a[i - 1] >= j - 1:
                graph[i].append(j)
    
    # Initialize a queue to store the students to be processed
    queue = [1]
    
    # Initialize a dictionary to store the messages to be sent
    messages = {}
    
    # Loop until the queue is empty
    while queue:
        # Get the student number from the queue
        student = queue.pop(0)
        
        # Loop through the students that the current student can send messages to
        for i in graph[student]:
            # If the message has not been sent before, add it to the dictionary
            if i not in messages:
                messages[i] = student
                queue.append(i)
    
    # Return the number of messages to be sent
    return len(messages)

def get_messages(n, a):
    # Get the plan of messages to be sent
    plan = get_plan(n, a)
    
    # Initialize an empty list to store the messages
    messages = []
    
    # Loop through the students that will send messages
    for i in range(1, n + 1):
        # If the student has a message to send, add it to the list
        if i in messages:
            messages.append([i, messages[i]])
    
    # Return the list of messages
    return messages

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_messages(n, a))

