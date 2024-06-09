
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
        return -1
    
    # Calculate the correct time
    correct_hours = (original_hours + hours_diff) % 24
    correct_minutes = (original_minutes + minutes_diff) % 60
    
    # Return the correct time
    return f"{correct_hours:02d}:{correct_minutes:02d}"

def get_all_correct_times(original_time, current_time):
    # Get the correct time
    correct_time = get_correct_time(original_time, current_time)
    
    # If the time is invalid, return an empty list
    if correct_time == -1:
        return []
    
    # Initialize a list to store the correct times
    correct_times = []
    
    # Add the original time and the correct time to the list
    correct_times.append(original_time)
    correct_times.append(correct_time)
    
    # Add all possible times between the original and correct times to the list
    for i in range(1, 24):
        for j in range(0, 60):
            time = f"{i:02d}:{j:02d}"
            if time != original_time and time != correct_time:
                correct_times.append(time)
    
    # Return the list of correct times
    return correct_times

def main():
    # Read the input
    original_time = input()
    current_time = input()
    
    # Get all the correct times
    correct_times = get_all_correct_times(original_time, current_time)
    
    # Print the number of correct times
    print(len(correct_times))
    
    # Print the correct times
    for time in correct_times:
        print(time)

if __name__ == '__main__':
    main()

