
def get_max_recordable_shows(tv_schedule, k):
    # Sort the TV schedule by start time
    tv_schedule.sort(key=lambda x: x[0])
    
    # Initialize the number of recordable shows to 0
    num_recordable_shows = 0
    
    # Iterate through the TV schedule
    for i in range(len(tv_schedule)):
        # Get the current show and its duration
        current_show = tv_schedule[i]
        current_show_duration = current_show[1] - current_show[0]
        
        # Check if the current show can be recorded in the next available slot
        if current_show_duration <= k:
            # Increment the number of recordable shows
            num_recordable_shows += 1
        else:
            # Calculate the number of slots required to record the current show
            num_slots_required = current_show_duration // k
            
            # Check if the current show can be recorded in the next available slots
            if num_slots_required <= k:
                # Increment the number of recordable shows
                num_recordable_shows += 1
            else:
                # The current show cannot be recorded, so break the loop
                break
    
    return num_recordable_shows

def main():
    # Read the input data
    n, k = map(int, input().split())
    tv_schedule = []
    for _ in range(n):
        tv_schedule.append(list(map(int, input().split())))
    
    # Call the function to get the maximum number of recordable shows
    max_recordable_shows = get_max_recordable_shows(tv_schedule, k)
    
    # Print the result
    print(max_recordable_shows)

if __name__ == '__main__':
    main()

