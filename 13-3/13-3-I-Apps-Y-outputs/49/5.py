
def f1(event_types):
    # Initialize a dictionary to store the counts of each event type
    event_counts = {}
    for event_type in event_types:
        if event_type not in event_counts:
            event_counts[event_type] = 1
        else:
            event_counts[event_type] += 1

    # Initialize a variable to store the total number of good itineraries
    total_good_itineraries = 0

    # Iterate over the event types and calculate the number of good itineraries for each type
    for event_type in event_counts:
        # Calculate the number of good itineraries for the current event type
        num_good_itineraries = event_counts[event_type] * (event_counts[event_type] - 1) // 2
        total_good_itineraries += num_good_itineraries

    return total_good_itineraries

