
def paint_picture(s):
    # Initialize the picture with all white squares
    picture = [["." for _ in range(len(s[0]))] for _ in range(len(s))]

    # Loop through each row and column
    for i in range(len(s)):
        for j in range(len(s[0])):
            # If the current square is a #, make it black
            if s[i][j] == "#":
                picture[i][j] = "#"
            # If the current square is a . and there is a black square in the same row or column, make it black
            elif s[i][j] == "." and (any(picture[i][k] == "#" for k in range(len(s[0]))) or any(picture[k][j] == "#" for k in range(len(s)))):
                picture[i][j] = "#"

    # Check if all the # squares are painted black
    return all(any(picture[i][j] == "#" for i in range(len(s))) for j in range(len(s[0])))

def main():
    s = [list(input()) for _ in range(int(input()))]
    print("Yes") if paint_picture(s) else print("No")

if __name__ == '__main__':
    main()

