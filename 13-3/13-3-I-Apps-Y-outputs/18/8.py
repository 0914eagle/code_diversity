
def get_major_scales(notes):
    notes = notes.split()
    scales = []
    for note in notes:
        for i in range(1, 12):
            scale = [note]
            for j in range(1, 8):
                scale.append(notes[(i+j)%12])
            if all(note in scale for note in notes):
                scales.append(scale)
    return sorted(list(set(scales)))

