
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_drinks = []
    
    # Iterate through the students
    for i in range(n):
        # If the current student has a favorite drink that is not in the current list of drinks, add it to the list
        if a[i] not in current_drinks:
            current_drinks.append(a[i])
            current_students += 1
        
        # If the current list of drinks has two drinks, calculate the maximum number of students that can be given these drinks
        if len(current_drinks) == 2:
            max_students = max(max_students, current_students)
            current_students = 0
            current_drinks = []
    
    # If there are an odd number of students, one portion will remain unused and the teacher will drink it
    if n % 2 == 1:
        max_students -= 1
    
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

