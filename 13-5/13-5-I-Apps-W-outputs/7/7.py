
def get_maximum_strength(students, clubs, d):
    # Initialize the maximum strength for each day
    max_strength = [0] * d

    # Loop through each day
    for day in range(d):
        # Get the students who have left their clubs on this day
        left_students = [student for student in students if student[2] == day + 1]

        # Get the clubs that have no members
        empty_clubs = [club for club in clubs if not club[1]]

        # Initialize the maximum strength for this day
        max_strength[day] = 0

        # Loop through each club
        for club in clubs:
            # If the club has no members, skip it
            if not club[1]:
                continue

            # Get the students in this club
            students_in_club = [student for student in students if student[1] == club[0]]

            # If the club has only one member, add their potential to the maximum strength
            if len(students_in_club) == 1:
                max_strength[day] += students_in_club[0][0]

            # If the club has more than one member, find the maximum strength among the students in the club
            else:
                # Get the potentials of the students in the club
                potentials = [student[0] for student in students_in_club]

                # Find the maximum strength among the potentials
                max_strength[day] += max(potentials)

        # Loop through each student who has left their club
        for student in left_students:
            # Get the club that the student left
            left_club = [club for club in clubs if club[0] == student[1]][0]

            # Remove the student from the club
            left_club[1].remove(student)

            # If the club has no members, add it to the list of empty clubs
            if not left_club[1]:
                empty_clubs.append(left_club)

        # Loop through each empty club
        for club in empty_clubs:
            # Add the club's potential to the maximum strength
            max_strength[day] += club[0]

            # Remove the club from the list of clubs
            clubs.remove(club)

    return max_strength

def main():
    # Read the input
    n, m = map(int, input().split())
    students = []
    for i in range(n):
        students.append(list(map(int, input().split())))
    d = int(input())
    left_students = [int(input()) for _ in range(d)]

    # Get the maximum strength for each day
    max_strength = get_maximum_strength(students, clubs, d)

    # Print the maximum strength for each day
    for day in range(d):
        print(max_strength[day])

if __name__ == '__main__':
    main()

