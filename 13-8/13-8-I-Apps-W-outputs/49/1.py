
def get_max_students_with_favorite_drink(n, k, a):
    # Calculate the minimum number of sets needed to give each student a drink
    min_sets = ceil(n / 2)
    
    # Create a dictionary to store the number of students with each drink type
    drink_counts = {}
    for i in range(n):
        if a[i] not in drink_counts:
            drink_counts[a[i]] = 1
        else:
            drink_counts[a[i]] += 1
    
    # Initialize the maximum number of students with a favorite drink to 0
    max_students = 0
    
    # Iterate over the drink types
    for drink in range(1, k + 1):
        # If the drink type has at least one student with it as their favorite drink
        if drink in drink_counts:
            # Calculate the number of students with this drink type
            num_students = drink_counts[drink]
            
            # If the number of students with this drink type is greater than the minimum number of sets needed
            if num_students > min_sets:
                # Calculate the number of students with a favorite drink
                max_students += min_sets
            else:
                # Calculate the number of students with a favorite drink
                max_students += num_students
    
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

