
def solve(n, d, b, a):
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    for i in range(n):
        students[i] = a[i]
    
    # Initialize the number of rooms with non-hidden students
    x_1 = 0
    x_2 = 0
    
    # Loop through each room
    for i in range(n):
        # Count the number of non-hidden students in the current room
        non_hidden_students = 0
        for j in range(i, n):
            non_hidden_students += students[j]
        
        # Check if the number of non-hidden students is different from b
        if non_hidden_students != b:
            # Increment the number of rooms with non-hidden students
            x_1 += 1
        
        # Move to the next room
        i += d
        if i > n:
            i = n
    
    # Return the minimal possible value of the maximum of x_i
    return min(x_1, x_2)

