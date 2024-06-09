
def get_major_scales(notes):
    notes = notes.split()
    scales = []
    for note in notes:
        for scale in ["A#", "C", "D#", "F", "G", "A"]:
            if note == scale:
                scales.append(scale)
                break
    return " ".join(scales)

