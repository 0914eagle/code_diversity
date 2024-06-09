
def get_correct_time(original_time, current_time):
    # Split the times into hours and minutes
    original_hours, original_minutes = original_time.split(":")
    current_hours, current_minutes = current_time.split(":")
    
    # Convert the hours and minutes to integers
    original_hours = int(original_hours)
    original_minutes = int(original_minutes)
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
    
    # Calculate the difference between the original time and the current time
    hours_difference = current_hours - original_hours
    minutes_difference = current_minutes - original_minutes
    
    # If the difference is negative, add 24 to the hours difference
    if hours_difference < 0:
        hours_difference += 24
    
    # If the difference is negative, add 60 to the minutes difference
    if minutes_difference < 0:
        minutes_difference += 60
    
    # Calculate the new time by adding the differences to the original time
    new_hours = original_hours + hours_difference
    new_minutes = original_minutes + minutes_difference
    
    # If the new hours are greater than 23, subtract 24
    if new_hours > 23:
        new_hours -= 24
    
    # If the new minutes are greater than 59, subtract 60
    if new_minutes > 59:
        new_minutes -= 60
    
    # Return the new time in the format hh:mm
    return f"{new_hours:02d}:{new_minutes:02d}"

def main():
    original_time = input("Enter the original time: ")
    current_time = input("Enter the current time: ")
    correct_time = get_correct_time(original_time, current_time)
    print(f"The correct time is: {correct_time}")

if __name__ == "__main__":
    main()

