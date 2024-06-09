
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
    num_telescopes, num_event_types = map(int, input().split())
    
    # Initialize a list to store the observations
    observations = []
    
    # Iterate over the number of telescopes
    for _ in range(num_telescopes):
        # Read the observation
        observation = input()
        
        # Add the observation to the list of observations
        observations.append(observation)
    
    # Get the event durations
    event_durations = get_event_durations(observations)
    
    # Check if the event durations are valid
    if any(event_duration < 1 or event_duration > 365 for event_duration in event_durations.values()):
        # If the event durations are not valid, print -1
        print(-1)
    else:
        # If the event durations are valid, print the event durations
        print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

