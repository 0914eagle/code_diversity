
def read_ints():
    return map(int, input().split())

def compare_ints(a, b):
    if a < b:
        return "<"
    elif a > b:
        return ">"
    else:
        return "="

if __name__ == '__main__':
    a, b = read_ints()
    print(compare_ints(a, b))

