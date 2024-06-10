
def get_unique_conversations(n, k, ids):
    # Initialize an empty list to store the unique conversations
    unique_conversations = []
    
    # Iterate through the list of IDs
    for i in range(n):
        # If the ID is not in the list of unique conversations, add it
        if ids[i] not in unique_conversations:
            unique_conversations.append(ids[i])
        # If the list of unique conversations is full, remove the last conversation and add the new ID
        elif len(unique_conversations) == k:
            unique_conversations.pop()
            unique_conversations.append(ids[i])
    
    return unique_conversations

def get_displayed_conversations(n, k, ids):
    # Initialize an empty list to store the displayed conversations
    displayed_conversations = []
    
    # Iterate through the list of IDs
    for i in range(n):
        # If the ID is not in the displayed conversations, add it to the first position
        if ids[i] not in displayed_conversations:
            displayed_conversations.insert(0, ids[i])
        # If the displayed conversations are full, remove the last conversation and add the new ID to the first position
        elif len(displayed_conversations) == k:
            displayed_conversations.pop()
            displayed_conversations.insert(0, ids[i])
    
    return displayed_conversations

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    
    unique_conversations = get_unique_conversations(n, k, ids)
    displayed_conversations = get_displayed_conversations(n, k, ids)
    
    print(len(displayed_conversations))
    print(*displayed_conversations)

if __name__ == '__main__':
    main()

