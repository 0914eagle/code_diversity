
import itertools

def get_number_of_candidate_strings(message):
    number_of_candidate_strings = 0
    for i in range(len(message)):
        for substring in itertools.combinations(message, i + 1):
            if substring == "nn" or substring == "uu":
                number_of_candidate_strings += 1
    return number_of_candidate_strings % (10**9 + 7)

