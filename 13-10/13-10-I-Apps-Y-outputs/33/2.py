
def solve(n, k, messages):
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
    result = solve(n, k, messages)
    print(len(result))
    print(*result)

if __name__ == '__main__':
    main()

