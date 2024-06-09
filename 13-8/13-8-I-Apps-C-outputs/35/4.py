
def get_returnable_rooms(n, s):
    returnable_rooms = 0
    for i in range(n):
        if s[i] == '<':
            if s[(i+1)%n] == '>':
                returnable_rooms += 1
        elif s[i] == '>':
            if s[(i-1)%n] == '<':
                returnable_rooms += 1
        else:
            returnable_rooms += 2
    return returnable_rooms

