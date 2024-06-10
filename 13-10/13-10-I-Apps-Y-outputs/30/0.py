
def get_hours_until_new_year(hour):
    # Calculate the number of hours until New Year
    hours_until_new_year = 24 - hour
    
    # Return the result
    return hours_until_new_year

def main():
    # Accept input from the user
    hour = int(input("Enter the hour: "))
    
    # Check if the input is valid
    if not (1 <= hour <= 23):
        print("Invalid input")
        return
    
    # Call the function to get the number of hours until New Year
    hours_until_new_year = get_hours_until_new_year(hour)
    
    # Print the result
    print(f"We have {hours_until_new_year} hours until New Year at {hour}:00 on 30th, December.")

if __name__ == '__main__':
    main()

