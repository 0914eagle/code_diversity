
def create_staff(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    for note in notes:
        staff[note[0] - 1] += "*" * note[1]
    return "\n".join(staff)

