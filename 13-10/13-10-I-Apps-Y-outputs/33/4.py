
def get_conversations(n, k, ids):
    conversations = []
    for i in range(n):
        if conversations and conversations[-1][0] == ids[i]:
            continue
        conversations.append([ids[i]])
        if len(conversations) > k:
            conversations.pop()
    return conversations

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    conversations = get_conversations(n, k, ids)
    print(len(conversations))
    print(*[conversation[0] for conversation in conversations])

if __name__ == '__main__':
    main()

