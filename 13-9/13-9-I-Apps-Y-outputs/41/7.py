
def get_rows_and_columns():
    return map(int, input().split())

def get_number_of_rows_and_columns_to_paint():
    return map(int, input().split())

def paint_cells(rows, columns, rows_to_paint, columns_to_paint):
    total_cells = rows * columns
    cells_to_paint = (rows_to_paint * columns) + (columns_to_paint * rows) - (rows_to_paint * columns_to_paint)
    return total_cells - cells_to_paint

def main():
    rows, columns = get_rows_and_columns()
    rows_to_paint, columns_to_paint = get_number_of_rows_and_columns_to_paint()
    print(paint_cells(rows, columns, rows_to_paint, columns_to_paint))

if __name__ == '__main__':
    main()

