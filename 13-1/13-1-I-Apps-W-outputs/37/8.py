
def get_dependencies(projects):
    # Initialize a set to store the dependencies
    dependencies = set()
    
    # Iterate through the projects
    for project in projects:
        # If the project is not the first project, add it to the dependencies
        if project != projects[0]:
            dependencies.add(project)
    
    # Return the dependencies
    return dependencies

