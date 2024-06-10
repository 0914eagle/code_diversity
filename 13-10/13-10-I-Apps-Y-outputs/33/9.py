
def get_conversation_list(n, k, messages):
    conversation_list = []
    for message in messages:
        if message not in conversation_list:
            conversation_list.append(message)
            if len(conversation_list) > k:
                conversation_list.pop(0)
    return conversation_list

def main():
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    conversation_list = get_conversation_list(n, k, messages)
    print(len(conversation_list))
    print(*conversation_list)

if __name__ == '__main__':
    main()

