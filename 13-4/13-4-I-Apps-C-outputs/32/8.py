
def get_correct_time(original_time, current_time):
    # Split the times into hours and minutes
    original_hours, original_minutes = original_time.split(":")
    current_hours, current_minutes = current_time.split(":")
    
    # Convert the hours and minutes to integers
    original_hours = int(original_hours)
    original_minutes = int(original_minutes)
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
    
    # Calculate the difference between the original and current time
    hours_diff = current_hours - original_hours
    minutes_diff = current_minutes - original_minutes
    
    # Check if the difference is valid
    if hours_diff < 0 or hours_diff > 23 or minutes_diff < 0 or minutes_diff > 59:
        return []
    
    # Create a list to store the correct times
    correct_times = []
    
    # Iterate through all possible hours and minutes
    for hour in range(0, 24):
        for minute in range(0, 60):
            # Check if the current hour and minute is a valid time
            if hour == original_hours and minute == original_minutes:
                continue
            
            # Check if the current hour and minute is a valid time after applying the difference
            if hour == current_hours and minute == current_minutes:
                continue
            
            # Add the current hour and minute to the list of correct times
            correct_times.append(f"{hour:02d}:{minute:02d}")
    
    return correct_times

def main():
    original_time = input("Enter the original time: ")
    current_time = input("Enter the current time: ")
    correct_times = get_correct_time(original_time, current_time)
    print(len(correct_times))
    for time in correct_times:
        print(time)

if __name__ == '__main__':
    main()

