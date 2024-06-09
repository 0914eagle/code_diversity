
def get_min_capacity(log):
    # Initialize a set to store the current visitors in the room
    visitors = set()
    # Initialize the minimum capacity variable
    min_capacity = 0
    # Iterate through the log
    for event in log:
        # If the event is "+ r_i", add the visitor to the set of current visitors
        if event.startswith("+"):
            visitors.add(int(event[2:]))
        # If the event is "- r_i", remove the visitor from the set of current visitors
        elif event.startswith("-"):
            visitors.remove(int(event[2:]))
        # Update the minimum capacity if the current number of visitors is less than the previous minimum
        min_capacity = min(min_capacity, len(visitors))
    # Return the minimum capacity
    return min_capacity

def main():
    log = input().split()
    print(get_min_capacity(log))

if __name__ == '__main__':
    main()

