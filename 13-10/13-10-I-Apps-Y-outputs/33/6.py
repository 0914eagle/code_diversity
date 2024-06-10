
def get_conversations(n, k, ids):
    conversations = []
    for i in range(n):
        if len(conversations) == k and conversations[k-1][0] != ids[i]:
            conversations.pop()
        conversations.insert(0, (ids[i],))
    return conversations[:k]

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    conversations = get_conversations(n, k, ids)
    print(len(conversations))
    print(*[conversation[0] for conversation in conversations])

if __name__ == '__main__':
    main()

