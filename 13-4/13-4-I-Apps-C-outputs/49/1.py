
def get_max_eligible_pupils(pupils):
    # Initialize a dictionary to store the preferred music style and favorite sport for each pupil
    preferences = {}
    for pupil in pupils:
        preferences[pupil[0]] = (pupil[1], pupil[2], pupil[3])

    # Initialize a set to store the eligible pupils
    eligible_pupils = set()

    # Iterate through the pupils and add them to the eligible set if they satisfy at least one of the requirements
    for pupil in pupils:
        for other_pupil in pupils:
            if pupil != other_pupil and pupil[0] != other_pupil[0]:
                if abs(pupil[1] - other_pupil[1]) > 40 or pupil[2] != other_pupil[2] or pupil[3] != other_pupil[3]:
                    eligible_pupils.add(pupil[0])
                    break

    return len(eligible_pupils)

