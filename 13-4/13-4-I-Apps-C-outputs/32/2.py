
def get_correct_time(original_time, current_time):
    # Split the times into hours and minutes
    original_hours, original_minutes = original_time.split(":")
    current_hours, current_minutes = current_time.split(":")
    
    # Convert the times to integers
    original_hours = int(original_hours)
    original_minutes = int(original_minutes)
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
    
    # Calculate the difference between the original and current time
    hours_difference = current_hours - original_hours
    minutes_difference = current_minutes - original_minutes
    
    # Check if the difference is valid
    if hours_difference < 0 or hours_difference > 23 or minutes_difference < 0 or minutes_difference > 59:
        return []
    
    # Create a list to store the correct times
    correct_times = []
    
    # Iterate through the possible hours and minutes
    for hour in range(0, 24):
        for minute in range(0, 60):
            # Check if the time is valid
            if hour == original_hours and minute == original_minutes:
                continue
            
            # Check if the time is within the difference
            if hour == original_hours + hours_difference and minute == original_minutes + minutes_difference:
                # Add the time to the list
                correct_times.append(f"{hour:02d}:{minute:02d}")
    
    return correct_times

def main():
    original_time = input("Enter the original time: ")
    current_time = input("Enter the current time: ")
    correct_times = get_correct_time(original_time, current_time)
    print(f"There are {len(correct_times)} different times seen on the clock when setting it correctly:")
    for time in correct_times:
        print(time)

if __name__ == '__main__':
    main()

