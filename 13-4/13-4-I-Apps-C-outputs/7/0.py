
def get_leader(n, m, logs):
    # Initialize a set to store the present participants
    present = set()
    
    # Iterate through the logs
    for log in logs:
        # If the log is a log on, add the participant to the set
        if log[0] == "+":
            present.add(int(log[1:]))
        # If the log is a log off, remove the participant from the set
        else:
            present.remove(int(log[1:]))
    
    # Return the number of participants in the set
    return len(present)

def main():
    # Read the input
    n, m = map(int, input().split())
    logs = [input() for _ in range(m)]
    
    # Call the get_leader function and print the result
    print(get_leader(n, m, logs))

if __name__ == '__main__':
    main()

