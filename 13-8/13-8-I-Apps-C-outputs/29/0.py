
def solve(kid_data):
    # Initialize variables
    num_kids = len(kid_data)
    teacher_ids = [kid[0] for kid in kid_data]
    preference_lists = [kid[1:] for kid in kid_data]
    
    # Find the smallest non-negative integer T such that there is a partitioning of the kids into three classes
    for T in range(num_kids):
        # Create a dictionary to keep track of the kids in each class
        class_dict = {0: [], 1: [], 2: []}
        
        # Add kids to their corresponding classes based on their preference lists
        for i, kid in enumerate(kid_data):
            # Get the current teacher and class for this kid
            current_teacher = teacher_ids[i]
            current_class = class_dict[current_teacher]
            
            # Add the kid to the class if it is in the top T places of their preference list
            if i in kid[1:T+1]:
                class_dict[current_teacher].append(i)
            # Otherwise, try to add the kid to a different class
            else:
                # Check if the kid can be added to any of the other classes
                for j in range(3):
                    if j != current_teacher and kid[1:T+1].issubset(class_dict[j]):
                        class_dict[j].append(i)
                        break
        
        # Check if all kids have been assigned to a class
        if all(len(class_dict[i]) == num_kids//3 for i in range(3)):
            return T
    
    # If no partitioning was found, return -1
    return -1

