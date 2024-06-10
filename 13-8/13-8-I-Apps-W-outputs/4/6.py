
def get_visible_messages(messages, k):
    visible_messages = set()
    for message in messages:
        if message.link_to:
            visible_messages.add(message.link_to)
        for i in range(1, k + 1):
            if message.link_to - i >= 0:
                visible_messages.add(message.link_to - i)
            if message.link_to + i <= len(messages):
                visible_messages.add(message.link_to + i)
    return visible_messages

def get_distinct_messages(messages, k):
    distinct_messages = set()
    for message in messages:
        if message.link_to:
            distinct_messages.add(message.link_to)
    return len(distinct_messages)

class Message:
    def __init__(self, link_to):
        self.link_to = link_to

def main():
    n, k = map(int, input().split())
    messages = [Message(int(i)) for i in input().split()]
    visible_messages = get_visible_messages(messages, k)
    distinct_messages = get_distinct_messages(visible_messages, k)
    print(distinct_messages)

if __name__ == '__main__':
    main()

