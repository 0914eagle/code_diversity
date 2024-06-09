
def check_containment(image_a, template_image):
    n_rows, n_cols = len(image_a), len(image_a[0])
    m_rows, m_cols = len(template_image), len(template_image[0])

    for row in range(n_rows - m_rows + 1):
        for col in range(n_cols - m_cols + 1):
            found_match = True
            for i in range(m_rows):
                for j in range(m_cols):
                    if template_image[i][j] != image_a[row + i][col + j]:
                        found_match = False
                        break
                if not found_match:
                    break
            if found_match:
                return True
    return False

def main():
    n_rows, n_cols = map(int, input().split())
    image_a = [input() for _ in range(n_rows)]
    template_image = [input() for _ in range(n_rows)]
    print("Yes") if check_containment(image_a, template_image) else print("No")

if __name__ == '__main__':
    main()
