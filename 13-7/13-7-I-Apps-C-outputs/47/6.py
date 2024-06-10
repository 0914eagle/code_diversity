
def get_min_empty_squares(N):
    # Initialize variables
    min_empty_squares = N
    for w in range(1, int(N**0.5) + 1):
        for h in range(w, int(N**0.5) + 1):
            if w * h >= N:
                break
            empty_squares = N - (w * h)
            if empty_squares < min_empty_squares:
                min_empty_squares = empty_squares
    return min_empty_squares

def main():
    N = int(input())
    print(get_min_empty_squares(N))

if __name__ == '__main__':
    main()

