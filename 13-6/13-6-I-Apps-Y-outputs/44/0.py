
def compare_magnitudes(a, b):
    if a > b:
        return "GREATER"
    elif a < b:
        return "LESS"
    else:
        return "EQUAL"

def main():
    a, b = map(int, input().split())
    print(compare_magnitudes(a, b))

if __name__ == '__main__':
    main()

