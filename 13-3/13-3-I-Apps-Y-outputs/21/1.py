
def create_staff(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    for note in notes:
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1
        line = " " * 24
        if pitch == "C":
            line = line[:2] + "*" * duration
        elif pitch == "D":
            line = line[4:6] + "*" * duration
        elif pitch == "E":
            line = line[8:10] + "*" * duration
        elif pitch == "F":
            line = line[12:14] + "*" * duration
        elif pitch == "G":
            line = line[16:18] + "*" * duration
        elif pitch == "A":
            line = line[20:22] + "*" * duration
        elif pitch == "B":
            line = line[24:26] + "*" * duration
        staff[pitch] = line
    return "\n".join(staff)

