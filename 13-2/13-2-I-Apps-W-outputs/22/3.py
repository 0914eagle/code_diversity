
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_drink = 1
    drink_count = [0] * (k + 1)
    
    # Iterate through the students
    for i in range(n):
        # If the current student has the current drink as their favorite, increment the count
        if a[i] == current_drink:
            current_students += 1
        # If the current student has a different drink as their favorite, or if we have reached the end of the list
        else:
            # If the current number of students with the current drink is greater than the maximum, update the maximum
            if current_students > max_students:
                max_students = current_students
            # Reset the current number of students and increment the current drink
            current_students = 1
            current_drink += 1
    
    # If the last group of students has the maximum number of students, update the maximum
    if current_students > max_students:
        max_students = current_students
    
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

