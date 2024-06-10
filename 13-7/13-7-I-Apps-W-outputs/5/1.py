
def get_message_plan(n, a):
    # Initialize a graph to represent the relationships between students
    graph = [[] for _ in range(n + 1)]
    
    # Add edges to the graph based on the maximum number of messages each student can send
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and a[i - 1] >= j - 1:
                graph[i].append(j)
    
    # Initialize a queue to store the students who need to send messages
    queue = [1]
    
    # Initialize a set to keep track of the students who have already sent messages
    sent = set()
    
    # Initialize a list to store the messages to be sent
    messages = []
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a student from the queue
        student = queue.pop(0)
        
        # If the student has not already sent a message, send a message to all their neighbors
        if student not in sent:
            for neighbor in graph[student]:
                messages.append((student, neighbor))
                queue.append(neighbor)
                sent.add(neighbor)
    
    # Return the list of messages
    return messages

def main():
    n = int(input())
    a = list(map(int, input().split()))
    messages = get_message_plan(n, a)
    print(len(messages))
    for message in messages:
        print(*message)

if __name__ == '__main__':
    main()

