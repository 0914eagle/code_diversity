
def get_major_scales(notes):
    notes = notes.split()
    scales = []
    for note in notes:
        for i in range(1, 13):
            scale = [note]
            for j in range(1, 8):
                scale.append(notes[(i+j)%12])
            if all(scale[j] == notes[j] for j in range(1, 8)):
                scales.append(note)
    return " ".join(scales) if scales else "none"

