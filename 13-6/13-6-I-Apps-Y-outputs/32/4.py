
def solve(article):
    # Split the article into rows and columns
    rows = article.split('\n')
    cols = [list(row) for row in rows]

    # Get the parameters for the scanner
    r, c, z_r, z_c = map(int, input().split())

    # Create a matrix to store the enlarged article
    enlarged_article = [['' for _ in range(c*z_c)] for _ in range(r*z_r)]

    # Loop through the original article and enlarge it
    for i in range(r):
        for j in range(c):
            char = cols[i][j]
            for k in range(z_r):
                for l in range(z_c):
                    enlarged_article[i*z_r+k][j*z_c+l] = char

    # Return the enlarged article
    return '\n'.join(''.join(row) for row in enlarged_article)

