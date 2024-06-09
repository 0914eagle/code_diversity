
def get_maximum_number_of_eligible_pupils(pupils):
    # Initialize a dictionary to store the preferred music style and favourite sport of each pupil
    preferences = {}
    for pupil in pupils:
        preferences[pupil[0]] = (pupil[1], pupil[2], pupil[3])

    # Initialize a list to store the eligible pupils
    eligible_pupils = []

    # Iterate through the list of pupils and check if they satisfy at least one of the requirements
    for pupil in pupils:
        height = pupil[0]
        sex = pupil[1]
        music_style = pupil[2]
        sport = pupil[3]
        is_eligible = False
        for other_pupil in pupils:
            if height != other_pupil[0] and sex != other_pupil[1] and music_style != other_pupil[2] and sport != other_pupil[3]:
                is_eligible = True
                break
        if is_eligible:
            eligible_pupils.append(pupil)

    return len(eligible_pupils)

