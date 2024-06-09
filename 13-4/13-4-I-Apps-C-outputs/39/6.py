
def get_event_durations(observations):
    # Initialize a dictionary to store the event durations
    event_durations = {}
    
    # Iterate over the observations
    for observation in observations:
        # Extract the start and end dates and the number of events observed
        start_date, end_date, num_events = observation
        
        # Convert the dates to integers
        start_date = int(start_date)
        end_date = int(end_date)
        
        # Calculate the duration of the event
        duration = end_date - start_date + 1
        
        # Add the duration to the event durations dictionary
        if num_events in event_durations:
            event_durations[num_events] += duration
        else:
            event_durations[num_events] = duration
    
    # Return the event durations dictionary
    return event_durations

def main():
    # Read the input
    num_telescopes, num_event_types = map(int, input().split())
    observations = []
    for _ in range(num_telescopes):
        observation = input().split()
        observations.append(observation)
    
    # Calculate the event durations
    event_durations = get_event_durations(observations)
    
    # Print the event durations
    print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

