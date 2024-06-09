
def get_major_scales(notes):
    notes = notes.split()
    scales = []
    for note in notes:
        for scale in ["A#", "C", "D#", "F", "G", "A"]:
            if note == scale[0] and all(note in notes for note in scale):
                scales.append(" ".join(scale))
    return "none" if not scales else " ".join(sorted(set(scales)))

