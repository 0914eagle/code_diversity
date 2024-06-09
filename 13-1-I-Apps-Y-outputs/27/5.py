
def is_possible(n, r, projects):
    # Sort the projects in descending order of rating required
    projects.sort(key=lambda x: x[0], reverse=True)
    # Initialize the current rating and the list of completed projects
    current_rating = r
    completed_projects = []
    # Iterate through the projects and check if the current rating is enough
    for project in projects:
        if current_rating >= project[0]:
            # If the current rating is enough, complete the project and update the current rating
            current_rating += project[1]
            completed_projects.append(project)
        else:
            # If the current rating is not enough, return False
            return False
    # If all the projects are completed, return True
    return True

