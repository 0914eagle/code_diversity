
def get_max_eligible_pupils(pupils):
    # Initialize a list to store the eligible pupils
    eligible_pupils = []

    # Iterate over the list of pupils
    for i in range(len(pupils)):
        # Get the current pupil's information
        height, gender, music_style, sport = pupils[i]

        # Check if the current pupil is eligible by comparing their information with the information of all the other pupils
        is_eligible = True
        for j in range(len(pupils)):
            if i != j:
                other_height, other_gender, other_music_style, other_sport = pupils[j]
                if abs(height - other_height) <= 40 and gender == other_gender and music_style == other_music_style and sport == other_sport:
                    is_eligible = False
                    break

        # If the current pupil is eligible, add them to the list of eligible pupils
        if is_eligible:
            eligible_pupils.append(i)

    # Return the maximum number of eligible pupils
    return len(eligible_pupils)

