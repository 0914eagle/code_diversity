
def get_leaders(n, m, messages):
    leaders = set()
    for message in messages:
        if message.startswith("+"):
            leaders.add(int(message[1:]))
        else:
            leaders.remove(int(message[1:]))
    return list(leaders)

