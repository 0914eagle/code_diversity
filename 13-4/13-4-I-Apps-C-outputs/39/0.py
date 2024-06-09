
def get_event_durations(observations):
    # Initialize a dictionary to store the event durations
    event_durations = {}
    
    # Iterate over the observations
    for observation in observations:
        # Extract the start and end dates and the number of events observed
        start_date, end_date, *event_counts = observation
        
        # Convert the dates to integers
        start_date = int(start_date)
        end_date = int(end_date)
        
        # Iterate over the event counts
        for event_index, event_count in enumerate(event_counts):
            # Check if the event has already been observed
            if event_index in event_durations:
                # If the event has been observed before, add the current duration to the total duration
                event_durations[event_index] += end_date - start_date
            else:
                # If the event has not been observed before, set the total duration to the current duration
                event_durations[event_index] = end_date - start_date
    
    # Return the event durations
    return event_durations

def main():
    # Read the number of telescopes and event types
    n_telescopes, n_event_types = map(int, input().split())
    
    # Read the observations
    observations = []
    for _ in range(n_telescopes):
        observations.append(list(map(int, input().split())))
    
    # Get the event durations
    event_durations = get_event_durations(observations)
    
    # Check if there is a solution
    if any(event_duration == 0 for event_duration in event_durations.values()):
        print(-1)
    else:
        # Print the event durations
        print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

