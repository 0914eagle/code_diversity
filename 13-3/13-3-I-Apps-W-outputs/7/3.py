
def get_max_height(notes):
    max_height = 0
    for note in notes:
        if note[1] > max_height:
            max_height = note[1]
    return max_height

def is_consistent(notes):
    for i in range(len(notes) - 1):
        if abs(notes[i][1] - notes[i+1][1]) > 1:
            return False
    return True

def main():
    n, m = map(int, input().split())
    notes = []
    for i in range(m):
        d, h = map(int, input().split())
        notes.append((d, h))
    if is_consistent(notes):
        print(get_max_height(notes))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()

