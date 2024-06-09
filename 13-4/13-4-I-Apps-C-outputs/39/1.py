
def get_event_durations(observations):
    # Initialize a dictionary to store the event durations
    event_durations = {}
    
    # Iterate over the observations
    for observation in observations:
        # Extract the start and end dates and the number of events observed
        start_date, end_date, *events = observation
        start_day, start_month = start_date
        end_day, end_month = end_date
        
        # Iterate over the events and update the event durations
        for event, count in zip(events, events):
            # If the event is not in the dictionary, add it with the duration of the current observation
            if event not in event_durations:
                event_durations[event] = count
            # Otherwise, add the duration of the current observation to the existing duration
            else:
                event_durations[event] += count
    
    # Return the event durations
    return event_durations

def main():
    # Read the input
    num_telescopes, num_event_types = map(int, input().split())
    observations = [tuple(map(int, input().split())) for _ in range(num_telescopes)]
    
    # Calculate the event durations
    event_durations = get_event_durations(observations)
    
    # Print the event durations
    print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

