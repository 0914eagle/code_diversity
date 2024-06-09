
def get_correct_time(original_time, current_time):
    # Split the times into hours and minutes
    original_hours, original_minutes = original_time.split(":")
    current_hours, current_minutes = current_time.split(":")
    
    # Convert the times to integers
    original_hours = int(original_hours)
    original_minutes = int(original_minutes)
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
    
    # Calculate the difference between the original and current times
    hours_diff = current_hours - original_hours
    minutes_diff = current_minutes - original_minutes
    
    # Check if the difference is valid
    if hours_diff < 0 or hours_diff > 23 or minutes_diff < 0 or minutes_diff > 59:
        return []
    
    # Initialize a list to store the correct times
    correct_times = []
    
    # Iterate through all possible hours and minutes
    for hour in range(0, 24):
        for minute in range(0, 60):
            # Check if the current hour and minute match the original time
            if hour == original_hours and minute == original_minutes:
                # Add the current time to the list of correct times
                correct_times.append(f"{hour:02d}:{minute:02d}")
    
    # Return the list of correct times
    return correct_times

def main():
    # Read the original time and current time from stdin
    original_time = input()
    current_time = input()
    
    # Call the get_correct_time function and store the result
    correct_times = get_correct_time(original_time, current_time)
    
    # Print the number of correct times
    print(len(correct_times))
    
    # Print each correct time on a new line
    for correct_time in correct_times:
        print(correct_time)

if __name__ == '__main__':
    main()

