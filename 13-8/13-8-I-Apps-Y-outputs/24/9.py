
def solve(s_a, s_b, s_c):
    while s_a or s_b or s_c:
        if s_a:
            s_a = s_a[1:]
            if s_a:
                next_player = s_a[0]
            else:
                return "A"
        elif s_b:
            s_b = s_b[1:]
            if s_b:
                next_player = s_b[0]
            else:
                return "B"
        else:
            s_c = s_c[1:]
            if s_c:
                next_player = s_c[0]
            else:
                return "C"
    return "D"

