
def is_visible(white_sheet, black_sheet1, black_sheet2):
    # Check if any point on the white sheet is outside both black sheets
    for x in range(white_sheet[0], white_sheet[2] + 1):
        for y in range(white_sheet[1], white_sheet[3] + 1):
            if not (black_sheet1[0] <= x <= black_sheet1[2] and black_sheet1[1] <= y <= black_sheet1[3]) and not (black_sheet2[0] <= x <= black_sheet2[2] and black_sheet2[1] <= y <= black_sheet2[3]):
                return "YES"
    return "NO"

