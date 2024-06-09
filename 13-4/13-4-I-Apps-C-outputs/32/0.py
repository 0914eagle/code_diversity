
def get_correct_time(original_time, current_time):
    # Split the times into hours and minutes
    original_hours, original_minutes = original_time.split(":")
    current_hours, current_minutes = current_time.split(":")
    
    # Convert the hours and minutes to integers
    original_hours = int(original_hours)
    original_minutes = int(original_minutes)
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
    
    # Calculate the difference between the original and current times
    hour_diff = current_hours - original_hours
    minute_diff = current_minutes - original_minutes
    
    # Check if the difference is valid
    if hour_diff < 0 or hour_diff > 23 or minute_diff < 0 or minute_diff > 59:
        return []
    
    # Create a list to store the correct times
    correct_times = []
    
    # Add the original time to the list
    correct_times.append(original_time)
    
    # Add the current time to the list
    correct_times.append(current_time)
    
    # Add the times that result from increasing the hour and minute by 1
    for i in range(hour_diff):
        correct_times.append(f"{original_hours + i:02d}:{original_minutes:02d}")
    for i in range(minute_diff):
        correct_times.append(f"{original_hours:02d}:{original_minutes + i:02d}")
    
    # Return the list of correct times
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

