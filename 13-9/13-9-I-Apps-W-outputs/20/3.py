
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

def can_form_triangle(segments):
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            for k in range(j+1, len(segments)):
                if is_triangle(segments[i], segments[j], segments[k]):
                    return True
    return False

segments = [int(x) for x in input().split()]
print("YES") if can_form_triangle(segments) else print("NO")

