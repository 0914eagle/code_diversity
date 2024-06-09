
def enlarge_article(article, z_rows, z_cols):
    enlarged_article = []
    for row in article:
        enlarged_row = []
        for char in row:
            enlarged_row += [char] * z_cols
        enlarged_article += [enlarged_row] * z_rows
    return enlarged_article

