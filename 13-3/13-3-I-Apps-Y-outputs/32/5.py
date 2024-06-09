
def is_template_contained(image_a, template):
    n_rows, n_cols = len(image_a), len(image_a[0])
    m_rows, m_cols = len(template), len(template[0])

    for i in range(n_rows - m_rows + 1):
        for j in range(n_cols - m_cols + 1):
            if template == image_a[i:i+m_rows][j:j+m_cols]:
                return True
    return False

def main():
    n_rows, n_cols = map(int, input().split())
    image_a = [input() for _ in range(n_rows)]
    template = [input() for _ in range(n_rows)]
    print("Yes") if is_template_contained(image_a, template) else print("No")

if __name__ == '__main__':
    main()

