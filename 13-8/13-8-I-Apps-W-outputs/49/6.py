
def get_max_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_drink = 1
    drink_sets = []
    
    # Iterate through each student
    for i in range(n):
        # If the current student has the current drink as their favorite, increase the number of current students
        if a[i] == current_drink:
            current_students += 1
        # If the current student does not have the current drink as their favorite, or if we have reached the end of the drink sets, move on to the next drink set
        else:
            # Add the current drink set to the list of drink sets
            drink_sets.append(current_drink)
            # If the current drink set has an even number of students, increase the maximum number of students
            if current_students % 2 == 0:
                max_students += current_students
            # If the current drink set has an odd number of students, increase the maximum number of students by one less than the number of students
            else:
                max_students += current_students - 1
            # Reset the current students and move on to the next drink set
            current_students = 1
            current_drink += 1
    
    # Add the last drink set to the list of drink sets
    drink_sets.append(current_drink)
    # If the last drink set has an even number of students, increase the maximum number of students
    if current_students % 2 == 0:
        max_students += current_students
    # If the last drink set has an odd number of students, increase the maximum number of students by one less than the number of students
    else:
        max_students += current_students - 1
    
    return max_students

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the function to get the maximum number of students with their favorite drink
    max_students = get_max_students_with_favorite_drink(n, k, a)
    
    # Print the result
    print(max_students)

if __name__ == '__main__':
    main()

