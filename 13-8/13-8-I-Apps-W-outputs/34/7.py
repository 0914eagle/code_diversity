
def read_input():
    return input().strip()

def compare_integers(a, b):
    if a == b:
        return "="
    elif a < b:
        return "<"
    else:
        return ">"

if __name__ == '__main__':
    a = read_input()
    b = read_input()
    print(compare_integers(a, b))

