
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
    
    # If the difference is more than 1 hour, set the hours to the correct value and set the minutes to 0
    if hours_diff > 1:
        hours = current_hours
        minutes = 0
    
    # If the difference is less than 1 hour, set the minutes to the correct value and set the hours to 0
    elif hours_diff < 1:
        hours = 0
        minutes = current_minutes
    
    # If the difference is 1 hour, set the hours and minutes to the correct values
    else:
        hours = current_hours
        minutes = current_minutes
    
    # Return the corrected time
    return f"{hours:02d}:{minutes:02d}"

def main():
    original_time = input("Enter the original time: ")
    current_time = input("Enter the current time: ")
    corrected_time = get_correct_time(original_time, current_time)
    print(f"The corrected time is: {corrected_time}")

if __name__ == '__main__':
    main()

