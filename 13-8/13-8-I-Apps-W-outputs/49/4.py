
def get_max_students_with_favorite_drink(n, k, student_preferences):
    # Initialize a dictionary to store the number of students with each favorite drink
    drink_counts = {i: 0 for i in range(1, k + 1)}

    # Iterate over the student preferences and increment the corresponding drink count
    for student in student_preferences:
        drink_counts[student] += 1

    # Find the drink with the maximum number of students who prefer it
    max_drink = max(drink_counts, key=drink_counts.get)

    # Return the number of students who prefer the maximum drink
    return drink_counts[max_drink]

def main():
    n, k = map(int, input().split())
    student_preferences = []
    for _ in range(n):
        student_preferences.append(int(input()))
    print(get_max_students_with_favorite_drink(n, k, student_preferences))

if __name__ == '__main__':
    main()

