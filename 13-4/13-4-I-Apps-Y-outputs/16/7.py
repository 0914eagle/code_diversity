
def convert_to_staff(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    for note in notes:
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1
        staff[ord(pitch) - ord("A")] += "*" * duration
    return "\n".join(staff)

