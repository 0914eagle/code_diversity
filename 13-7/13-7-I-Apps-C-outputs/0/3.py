
def get_expected_severity(bugs, hours, faith_loss_factor):
    # Initialize the variables
    fixed_bugs = []
    unfixed_bugs = bugs
    total_severity = 0
    hour = 0
    
    # Loop through the hours
    while hour < hours:
        # Choose the bug to work on
        bug_to_work_on = choose_bug_to_work_on(unfixed_bugs)
        
        # Fix the bug
        if fix_bug(bug_to_work_on, faith_loss_factor):
            # If the bug is fixed, add its severity to the total severity and remove it from the unfixed bugs list
            total_severity += bug_to_work_on[1]
            fixed_bugs.append(bug_to_work_on)
            unfixed_bugs.remove(bug_to_work_on)
        hour += 1
    
    # Return the expected total severity of fixed bugs
    return total_severity

def choose_bug_to_work_on(unfixed_bugs):
    # Choose the bug with the highest probability of being fixed
    return max(unfixed_bugs, key=lambda x: x[0])

def fix_bug(bug, faith_loss_factor):
    # Fix the bug with probability equal to its initial probability of being fixed
    return random.random() <= bug[0]

if __name__ == '__main__':
    bugs = []
    hours = int(input())
    faith_loss_factor = float(input())
    
    # Read the bugs from standard input
    for _ in range(hours):
        bug = list(map(float, input().split()))
        bugs.append(bug)
    
    # Calculate the expected total severity of fixed bugs
    expected_severity = get_expected_severity(bugs, hours, faith_loss_factor)
    
    # Print the expected total severity of fixed bugs
    print(expected_severity)

