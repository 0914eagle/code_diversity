
def process_messages(n, k, messages):
    conversations = []
    for message in messages:
        if message not in conversations:
            conversations.append(message)
            if len(conversations) > k:
                conversations.pop(0)
    return conversations

def get_displayed_conversations(n, k, messages):
    conversations = process_messages(n, k, messages)
    return len(conversations), conversations

if __name__ == '__main__':
    n, k = map(int, input().split())
    messages = [int(input()) for _ in range(n)]
    m, displayed_conversations = get_displayed_conversations(n, k, messages)
    print(m)
    print(*displayed_conversations)

