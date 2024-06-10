
def is_possible(projects, rating):
    # Initialize a list to store the projects that Polycarp has completed
    completed_projects = []
    
    # Iterate through the projects
    for project in projects:
        # Check if Polycarp has enough rating to complete the current project
        if rating >= project[0]:
            # If he does, complete the project and update his rating
            rating += project[1]
            completed_projects.append(project)
        else:
            # If he doesn't, return False
            return False
    
    # If all projects are completed, return True
    return True

def main():
    # Read the input
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    
    # Check if it is possible to complete all projects
    if is_possible(projects, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

