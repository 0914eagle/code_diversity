
def get_leader_candidates(n_participants, log_messages):
    leader_candidates = set()
    for message in log_messages:
        if message.startswith("+"):
            leader_candidates.add(int(message[1:]))
        else:
            leader_candidates.remove(int(message[1:]))
    return leader_candidates

def get_leaders(n_participants, log_messages):
    leader_candidates = get_leader_candidates(n_participants, log_messages)
    leaders = []
    for candidate in leader_candidates:
        if any(message.startswith(str(candidate)) for message in log_messages):
            leaders.append(candidate)
    return leaders

def main():
    n_participants, n_messages = map(int, input().split())
    log_messages = []
    for _ in range(n_messages):
        log_messages.append(input())
    leaders = get_leaders(n_participants, log_messages)
    print(len(leaders))
    print(" ".join(str(leader) for leader in leaders))

if __name__ == '__main__':
    main()

