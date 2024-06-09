
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_drink = 1
    drink_count = [0] * (k + 1)
    drink_pairs = []

    # Iterate through the students' preferences
    for i in range(n):
        # If the current student's preference is not the current drink, move on to the next drink
        if a[i] != current_drink:
            continue

        # If the current drink is not in the list of drink pairs, add it
        if current_drink not in drink_pairs:
            drink_pairs.append(current_drink)

        # Increment the count of the current drink
        drink_count[current_drink] += 1

        # If the count of the current drink is 2, move on to the next drink
        if drink_count[current_drink] == 2:
            current_drink += 1
            drink_count[current_drink] = 0

        # Increment the number of students who have received a drink
        current_students += 1

        # If the number of students who have received a drink is equal to the ceiling of n/2, update the maximum number of students
        if current_students == int(n/2) + 1:
            max_students = max(max_students, current_students)

    # Return the maximum number of students who can get their favorite drink
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

