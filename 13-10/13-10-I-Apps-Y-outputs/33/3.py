
def get_conversations(n, k, ids):
    conversations = []
    for i in range(n):
        if len(conversations) == 0 or conversations[-1] != ids[i]:
            conversations.append(ids[i])
        if len(conversations) > k:
            conversations.pop(0)
    return conversations

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    conversations = get_conversations(n, k, ids)
    print(len(conversations))
    print(*conversations)

if __name__ == '__main__':
    main()

