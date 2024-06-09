
def get_experience_and_money(projects, p, q):
    # Initialize variables
    experience = 0
    money = 0
    
    # Iterate through the projects
    for project in projects:
        # Calculate the daily experience and money for the current project
        daily_experience = project[0]
        daily_money = project[1]
        
        # Check if the current project will help Mikhail achieve his dreams
        if daily_experience + experience >= p and daily_money + money >= q:
            # If it will, return the number of days needed
            return (p - experience) / daily_experience + (q - money) / daily_money
    
    # If none of the projects will help Mikhail achieve his dreams, return -1
    return -1

def solve(n, p, q, projects):
    # Sort the projects by their daily experience and money in descending order
    projects.sort(key=lambda x: x[0], reverse=True)
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
        
        # Check if the current project will help Mikhail achieve his dreams
        if daily_experience + experience >= p and daily_money + money >= q:
            # If it will, add the number of days needed for the current project to the total number of days
            days += (p - experience) / daily_experience + (q - money) / daily_money
            experience += daily_experience
            money += daily_money
    
    # Return the total number of days needed
    return days

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append([a, b])
    print(solve(n, p, q, projects))

