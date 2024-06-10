
def get_conversations(n, k, messages):
    conversations = []
    for message in messages:
        if message in conversations:
            continue
        conversations.append(message)
        if len(conversations) > k:
            conversations.pop()
    return conversations

def main():
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    conversations = get_conversations(n, k, messages)
    print(len(conversations))
    print(*conversations)

if __name__ == '__main__':
    main()

