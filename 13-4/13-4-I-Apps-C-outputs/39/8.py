
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
                # If the event has already been observed, add the current observation to the total duration
                event_durations[event_index] += (end_date - start_date) * event_count
            else:
                # If the event has not been observed before, set the duration to the current observation
                event_durations[event_index] = (end_date - start_date) * event_count
    
    # Return the event durations
    return event_durations

def main():
    # Read the number of telescopes and event types
    num_telescopes, num_event_types = map(int, input().split())
    
    # Read the observations
    observations = []
    for _ in range(num_telescopes):
        observations.append(list(map(int, input().split())))
    
    # Calculate the event durations
    event_durations = get_event_durations(observations)
    
    # Print the event durations
    print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

