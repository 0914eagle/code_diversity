
def get_major_scales(notes):
    notes = notes.split()
    scales = []
    for note in notes:
        for i in range(1, 13):
            scale = [note]
            for j in range(1, 8):
                if (i + j) % 12 == 0:
                    break
                scale.append(notes[(i + j) % 12])
            if set(scale) == set(notes):
                scales.append(note)
    if not scales:
        return "none"
    return " ".join(sorted(scales))

