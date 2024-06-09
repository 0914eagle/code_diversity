
def solve(n, t, a):
    # Calculate the total time Luba has to spend on work
    total_work_time = sum(a)
    
    # Calculate the number of days Luba can finish reading the book
    days_to_read = t // 86400
    
    # Initialize the minimum number of days to finish reading the book as the number of days Luba can finish reading the book
    min_days = days_to_read
    
    # Iterate over each day
    for i in range(n):
        # Calculate the total time Luba has to spend on work and reading for the current day
        current_work_time = a[i]
        current_reading_time = t - current_work_time
        
        # If the total time is less than the number of days to read the book, update the minimum number of days to finish reading the book
        if current_work_time + current_reading_time < min_days:
            min_days = current_work_time + current_reading_time
    
    return min_days

