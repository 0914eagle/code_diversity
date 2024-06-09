
def get_experience_and_money(projects, p, q):
    # Initialize variables
    experience = 0
    money = 0
    
    # Iterate over the projects
    for project in projects:
        # Calculate the daily increase in experience and money
        daily_experience = project[0]
        daily_money = project[1]
        
        # Check if working on this project will give Mikhail enough experience and money
        if experience + daily_experience >= p and money + daily_money >= q:
            # If so, return the number of days needed
            return (p - experience) / daily_experience + (q - money) / daily_money
    
    # If Mikhail cannot get enough experience and money by working on any project, return -1
    return -1

def solve(n, p, q, projects):
    # Sort the projects by their daily income
    projects.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize variables
    days = 0
    experience = 0
    money = 0
    
    # Iterate over the projects
    for project in projects:
        # Calculate the daily increase in experience and money
        daily_experience = project[0]
        daily_money = project[1]
        
        # Check if working on this project will give Mikhail enough experience and money
        if experience + daily_experience >= p and money + daily_money >= q:
            # If so, return the number of days needed
            return days + (p - experience) / daily_experience + (q - money) / daily_money
        
        # If not, update the variables and increment the number of days
        experience += daily_experience
        money += daily_money
        days += 1
    
    # If Mikhail cannot get enough experience and money by working on any project, return -1
    return -1

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append([a, b])
    print(solve(n, p, q, projects))

