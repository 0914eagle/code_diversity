
def get_experience_and_money(projects, p, q):
    # Initialize variables
    experience = 0
    money = 0
    
    # Iterate through the projects
    for project in projects:
        # Calculate the daily experience and money for the current project
        daily_experience = project[0]
        daily_money = project[1]
        
        # Check if working on the current project will bring Mikhail closer to his dreams
        if experience + daily_experience >= p and money + daily_money >= q:
            # If so, return the number of days needed to achieve his dreams
            return (p - experience) / daily_experience + (q - money) / daily_money
    
    # If Mikhail cannot achieve his dreams with any project, return -1
    return -1

def solve(n, p, q, projects):
    # Sort the projects by their daily income
    projects.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize variables
    days = 0
    experience = 0
    money = 0
    
    # Iterate through the projects
    for project in projects:
        # Calculate the daily experience and money for the current project
        daily_experience = project[0]
        daily_money = project[1]
        
        # Check if working on the current project will bring Mikhail closer to his dreams
        if experience + daily_experience >= p and money + daily_money >= q:
            # If so, add the number of days needed to achieve his dreams to the total number of days
            days += (p - experience) / daily_experience + (q - money) / daily_money
            experience += daily_experience
            money += daily_money
    
    # Return the total number of days needed to achieve Mikhail's dreams
    return days

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append([a, b])
    print(solve(n, p, q, projects))

