
def solve(n, preferences):
    # Initialize the variables
    teachers = [0, 0, 0]
    classes = [[], [], []]
    same_teacher_count = 0
    same_class_count = 0
    top_t = 0

    # Loop through each kid and their preference list
    for i in range(n):
        teacher, preference_list = preferences[i]

        # Check if the kid has the same teacher as last year
        if teacher == teachers[i]:
            same_teacher_count += 1

        # Check if the kid is in the same class as last year
        if classes[teacher].count(i) > 0:
            same_class_count += 1

        # Find the top T places of the preference list
        top_t = max(top_t, len(preference_list))

    # Return the smallest non-negative integer T that satisfies the conditions
    return max(0, top_t - same_teacher_count - same_class_count)

