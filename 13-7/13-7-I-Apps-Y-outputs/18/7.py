
def convert_to_staff_notation(notes):
    staff_notation = ""
    for note in notes:
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1
        staff_notation += pitch * duration + " "
    return staff_notation.strip()

def create_staff_lines(staff_notation):
    staff_lines = []
    for line in staff_notation.split("\n"):
        staff_lines.append(line.ljust(80, " "))
    return staff_lines

def create_staff(staff_lines):
    staff = ""
    for line in staff_lines:
        staff += line + "\n"
    return staff

def main():
    notes = input("Enter the notes: ").split()
    staff_notation = convert_to_staff_notation(notes)
    staff_lines = create_staff_lines(staff_notation)
    staff = create_staff(staff_lines)
    print(staff)

if __name__ == '__main__':
    main()

