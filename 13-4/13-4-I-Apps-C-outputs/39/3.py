
def get_event_durations(observations):
    # Initialize a dictionary to store the event durations
    event_durations = {}
    
    # Iterate over the observations
    for observation in observations:
        # Extract the start and end dates and the number of events observed
        start_date, end_date, *events = observation
        start_day, start_month = start_date
        end_day, end_month = end_date
        
        # Calculate the duration of the event
        duration = (end_day - start_day) + (end_month - start_month) * 30
        
        # Update the event durations dictionary
        for event, count in zip(events, events):
            if event not in event_durations:
                event_durations[event] = count * duration
            else:
                event_durations[event] += count * duration
    
    return event_durations

def main():
    # Read the number of telescopes and event types
    n_telescopes, n_event_types = map(int, input().split())
    
    # Read the observations
    observations = []
    for _ in range(n_telescopes):
        observations.append(list(map(int, input().split())))
    
    # Calculate the event durations
    event_durations = get_event_durations(observations)
    
    # Print the event durations
    print(*event_durations.values(), sep='\n')

if __name__ == '__main__':
    main()

