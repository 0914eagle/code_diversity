
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def can_form_triangle(line_segments):
    for i in range(len(line_segments)):
        for j in range(i+1, len(line_segments)):
            for k in range(j+1, len(line_segments)):
                if is_triangle(line_segments[i], line_segments[j], line_segments[k]):
                    return "YES"
    return "NO"

