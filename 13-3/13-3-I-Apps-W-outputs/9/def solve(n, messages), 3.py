
def solve(n, messages):
    chat_list = []
    for message in messages:
        if message not in chat_list:
            chat_list.insert(0, message)
        else:
            chat_list.remove(message)
            chat_list.insert(0, message)
    return chat_list

