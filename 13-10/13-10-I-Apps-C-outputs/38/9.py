
def get_leaders(n, log_on_off):
    # Initialize a set to store the leaders
    leaders = set()
    
    # Iterate through the log on/off messages
    for message in log_on_off:
        # If the message is a log on message, add the person to the leaders set
        if message.startswith("+"):
            leaders.add(int(message[1:]))
        # If the message is a log off message, remove the person from the leaders set
        elif message.startswith("-"):
            leaders.remove(int(message[1:]))
    
    # Return the number of leaders and the leaders in increasing order
    return len(leaders), sorted(leaders)

def main():
    n, m = map(int, input().split())
    log_on_off = [input() for _ in range(m)]
    k, leaders = get_leaders(n, log_on_off)
    print(k)
    print(*leaders)

if __name__ == '__main__':
    main()

