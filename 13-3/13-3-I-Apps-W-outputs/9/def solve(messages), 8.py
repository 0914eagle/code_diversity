
def solve(messages):
    chats = []
    for message in messages:
        if message not in chats:
            chats.insert(0, message)
        else:
            chats.remove(message)
            chats.insert(0, message)
    return chats

