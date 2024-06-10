
def get_conversations(n, k, ids):
    conversations = []
    for i in range(n):
        if len(conversations) < k or conversations[-1] != ids[i]:
            conversations.insert(0, ids[i])
            conversations = conversations[:k]
    return conversations

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    conversations = get_conversations(n, k, ids)
    print(len(conversations))
    print(*conversations)

if __name__ == '__main__':
    main()

