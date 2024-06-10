
def create_staff(notes):
    staff = 
    return staff

def create_note(note, duration):
    note_duration = ''
    for i in range(duration):
        note_duration += '*'
    return note_duration

def create_song(song):
    staff = create_staff(song)
    notes = song.split()
    for note in notes:
        pitch = note[0]
        duration = 1
        if len(note) > 1:
            duration = int(note[1])
        staff = staff.replace('*', create_note(pitch, duration), 1)
    return staff

if __name__ == '__main__':
    song = input()
    print(create_song(song))

