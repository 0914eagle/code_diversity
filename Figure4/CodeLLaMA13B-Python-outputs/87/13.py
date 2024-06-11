def get_row(lst, x):
    
    return sorted([(i, j) for i, row in enumerate(lst) for j in range(len(row) - 1, -1, -1) if row[j] == x], key=lambda x: x[0])

if __name__ == '__main__':
    print("Example:")
    print(list(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1)) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert list(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 3)) == [(0, 2), (1, 1), (2, 2)]
    assert list(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1