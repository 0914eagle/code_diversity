
def find_late_brother(a, b):
    late_brother = 0
    if a == 1:
        late_brother = 3
    elif a == 2:
        late_brother = 1
    else:
        late_brother = 2
    return late_brother

