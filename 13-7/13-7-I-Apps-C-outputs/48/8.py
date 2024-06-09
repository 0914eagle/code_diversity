
def solve(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    a.sort(reverse=True)
    
    # Initialize the number of passes given to each student to 0
    passes = [0] * n
    
    # Initialize the number of days needed to fix all bugs to 0
    days = 0
    
    # Loop through each bug and find the student who can fix it
    for i in range(m):
        # Find the student with the highest level of ability who can fix the current bug
        for j in range(n):
            if b[j] >= a[i]:
                # Assign the current bug to the current student
                passes[j] += 1
                break
        
        # Increment the number of days needed to fix all bugs
        days += 1
    
    # Check if the total number of passes given to the students exceeds the maximum allowed by the university
    if sum(passes) > s:
        return "NO"
    
    # Return the schedule of work
    return "YES\n" + " ".join(map(str, passes))

