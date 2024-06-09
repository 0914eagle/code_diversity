
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
    hours_diff = current_hours - original_hours
    minutes_diff = current_minutes - original_minutes
    
    # If the difference is negative, add 24 to the hours difference
    if hours_diff < 0:
        hours_diff += 24
    
    # If the difference is negative, add 60 to the minutes difference
    if minutes_diff < 0:
        minutes_diff += 60
    
    # Calculate the new time
    new_hours = original_hours + hours_diff
    new_minutes = original_minutes + minutes_diff
    
    # Format the new time as a string
    new_time = f"{new_hours:02d}:{new_minutes:02d}"
    
    return new_time

def main():
    original_time = input("Enter the original time: ")
    current_time = input("Enter the current time: ")
    new_time = get_correct_time(original_time, current_time)
    print(f"The new time is: {new_time}")

if __name__ == '__main__':
    main()

