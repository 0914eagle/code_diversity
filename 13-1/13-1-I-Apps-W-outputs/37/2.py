
def get_dependencies(projects):
    # Initialize a set to store the dependencies
    dependencies = set()
    
    # Iterate through the projects
    for project in projects:
        # If the project is not Polycarp's project, add it to the dependencies set
        if project != "a":
            dependencies.add(project)
    
    # Return the dependencies set
    return dependencies

