
def largest_rectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                area = 0
                for k in range(i, rows):
                    if matrix[k][j] == "1":
                        area += 1
                    else:
                        break
                max_area = max(max_area, area)
    return max_area

def main():
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(largest_rectangle(matrix))

if __name__ == '__main__':
    main()

