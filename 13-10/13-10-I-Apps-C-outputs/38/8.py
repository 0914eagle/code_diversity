
def get_leaders(participants, log_messages):
    leaders = set()
    for message in log_messages:
        if message[0] == "+":
            leaders.add(int(message[1:]))
        else:
            leaders.remove(int(message[1:]))
    return leaders

def get_leaders_from_whole_meeting(participants, log_messages):
    leaders = set()
    for message in log_messages:
        if message[0] == "+":
            leaders.add(int(message[1:]))
        else:
            leaders.remove(int(message[1:]))
    return leaders

def main():
    participants, log_messages = read_input()
    leaders = get_leaders(participants, log_messages)
    print(len(leaders))
    print(*sorted(leaders), sep=" ")

def read_input():
    participants = int(input())
    log_messages = int(input())
    log_messages = [input() for _ in range(log_messages)]
    return participants, log_messages

if __name__ == '__main__':
    main()

