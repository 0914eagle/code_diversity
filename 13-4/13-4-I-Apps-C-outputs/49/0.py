
def get_maximum_number_of_eligible_pupils(pupils):
    # Initialize a dictionary to store the number of eligible pupils for each music style
    music_style_count = {}
    # Initialize a dictionary to store the number of eligible pupils for each sport
    sport_count = {}

    for pupil in pupils:
        # Get the height, sex, music style, and sport of the current pupil
        height, sex, music_style, sport = pupil

        # Check if the current pupil is eligible based on the rules provided
        eligible = True
        if sex == "M" and height > 350:
            eligible = False
        if music_style in music_style_count and music_style_count[music_style] > 0:
            eligible = False
        if sport in sport_count and sport_count[sport] > 0:
            eligible = False

        # Update the dictionary counts for the current pupil's music style and sport
        if eligible:
            if music_style not in music_style_count:
                music_style_count[music_style] = 0
            music_style_count[music_style] += 1
            if sport not in sport_count:
                sport_count[sport] = 0
            sport_count[sport] += 1

    # Find the maximum number of eligible pupils by finding the maximum number of pupils for each music style and sport
    maximum_number_of_eligible_pupils = 0
    for music_style, count in music_style_count.items():
        maximum_number_of_eligible_pupils = max(maximum_number_of_eligible_pupils, count)
    for sport, count in sport_count.items():
        maximum_number_of_eligible_pupils = max(maximum_number_of_eligible_pupils, count)

    return maximum_number_of_eligible_pupils

