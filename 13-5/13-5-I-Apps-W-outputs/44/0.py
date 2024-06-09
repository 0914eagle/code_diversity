
def find_late_brother(a, b):
    late_brother = 0
    if a == 1:
        late_brother = 3 - b
    else:
        late_brother = 3 - a
    return late_brother

