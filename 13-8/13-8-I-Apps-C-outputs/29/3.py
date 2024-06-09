
def find_best_partition(preference_lists):
    # Initialize the number of teachers and the number of kids
    num_teachers = 3
    num_kids = len(preference_lists)
    
    # Initialize the count of kids in each class
    class_counts = [0] * num_teachers
    
    # Initialize the list of kids in each class
    classes = [[0] * num_kids for _ in range(num_teachers)]
    
    # Loop through each kid and their preference list
    for kid, preference_list in enumerate(preference_lists):
        # Find the teacher with the lowest number of kids
        min_teacher = 0
        for teacher in range(1, num_teachers):
            if class_counts[teacher] < class_counts[min_teacher]:
                min_teacher = teacher
        
        # Add the kid to the class with the lowest number of kids
        classes[min_teacher][class_counts[min_teacher]] = kid
        class_counts[min_teacher] += 1
    
    # Return the number of kids in each class
    return class_counts

