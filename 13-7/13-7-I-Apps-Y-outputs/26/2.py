
def get_order(projects, rating):
    # Initialize a list to store the order of projects
    order = []
    
    # Loop through the projects
    for project in projects:
        # Check if the current rating is greater than or equal to the required rating for the current project
        if rating >= project[0]:
            # If it is, add the project to the order and subtract the required rating from the current rating
            order.append(project)
            rating -= project[0]
        else:
            # If it's not, return False
            return False
    
    # If all projects are completed successfully, return the order
    return order

def main():
    # Read the number of projects and the initial rating from stdin
    n, r = map(int, input().split())
    
    # Read the projects from stdin
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    
    # Call the get_order function and print the result
    print("YES") if get_order(projects, r) else print("NO")

if __name__ == '__main__':
    main()

