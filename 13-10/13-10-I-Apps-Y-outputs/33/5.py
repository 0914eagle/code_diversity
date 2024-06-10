
def get_conversations(n, k, messages):
    conversations = []
    for message in messages:
        if message in conversations:
            continue
        elif len(conversations) == k:
            conversations.pop()
        conversations.insert(0, message)
    return conversations[:k]

def main():
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    conversations = get_conversations(n, k, messages)
    print(len(conversations))
    print(*conversations)

if __name__ == '__main__':
    main()

