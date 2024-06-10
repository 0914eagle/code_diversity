
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return note
    else:
        return note.lower()

def get_note_staff(note):
    staff = {
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'a': 'A',
        'b': 'B'
    }
    return staff[note.lower()]

def get_note_symbol(note):
    return '*' * get_note_duration(note)

def get_note_position(note):
    positions = {
        'C': 5,
        'D': 4,
        'E': 3,
        'F': 2,
        'G': 1,
        'A': 0,
        'B': -1
    }
    return positions[get_note_staff(note)]

def get_staff_line(note):
    staff_line = {
        'C': 'G:',
        'D': 'F:',
        'E': 'E:',
        'F': 'D:',
        'G': 'C:',
        'A': 'B:',
        'B': 'A:'
    }
    return staff_line[get_note_staff(note)]

def get_staff_symbol(note):
    staff_symbol = {
        'C': '|',
        'D': '|',
        'E': '|',
        'F': '|',
        'G': '|',
        'A': '|',
        'B': '|'
    }
    return staff_symbol[get_note_staff(note)]

def get_staff_padding(note):
    staff_padding = {
        'C': ' ',
        'D': ' ',
        'E': ' ',
        'F': ' ',
        'G': ' ',
        'A': ' ',
        'B': ' '
    }
    return staff_padding[get_note_staff(note)]

def get_note_staff_position(note):
    return get_note_position(note) - get_staff_position(note)

def get_staff_position(note):
    staff_position = {
        'C': 0,
        'D': 1,
        'E': 2,
        'F': 3,
        'G': 4,
        'A': 5,
        'B': 6
    }
    return staff_position[get_note_staff(note)]

def render_staff(notes):
    staff = []
    for note in notes:
        staff.append(get_staff_line(note))
        staff.append(get_staff_symbol(note) * get_note_duration(note))
        staff.append(get_staff_padding(note) * (get_note_staff_position(note) - 1))
        staff.append(get_note_symbol(note))
    return '\n'.join(staff)

def main():
    notes = input().split()
    print(render_staff(notes))

if __name__ == '__main__':
    main()

