
def get_max_melody_length(notes):
    max_length = 0
    for i in range(len(notes)):
        for j in range(i+1, len(notes)):
            if is_melody(notes[i:j]):
                max_length = max(max_length, j-i)
    return max_length

def is_melody(subsequence):
    for i in range(len(subsequence)-1):
        if abs(subsequence[i]-subsequence[i+1]) not in [1, 7]:
            return False
    return True

notes = [1, 2, 4, 5]
print(get_max_melody_length(notes))

notes = [62, 22, 60, 61, 48, 49]
print(get_max_melody_length(notes))

