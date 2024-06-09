
def solve(names, pseudonyms):
    # Initialize a dictionary to store the mapping of students to pseudonyms
    mapping = {}
    # Initialize a variable to store the maximum quality of matching
    max_quality = 0
    # Loop through each student and pseudonym
    for student, pseudonym in zip(names, pseudonyms):
        # Find the length of the largest common prefix between the student's name and the pseudonym
        lcp = len(set(student) & set(pseudonym))
        # If the length of the largest common prefix is greater than the current maximum quality, update the maximum quality and the mapping
        if lcp > max_quality:
            max_quality = lcp
            mapping = {student: pseudonym}
        # If the length of the largest common prefix is equal to the current maximum quality, add the student and pseudonym to the mapping
        elif lcp == max_quality:
            mapping[student] = pseudonym
    # Return the maximum quality and the mapping
    return max_quality, mapping

