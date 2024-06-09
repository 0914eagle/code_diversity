
def convert_to_staff_notation(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    for note in notes:
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1
        staff_line = staff[("cdefgab".index(pitch.lower()) - 1) * 2]
        staff[staff.index(staff_line)] = staff_line + "*" * duration
    return "\n".join(staff)

def main():
    notes = input("Enter the notes: ").split()
    print(convert_to_staff_notation(notes))

if __name__ == '__main__':
    main()

