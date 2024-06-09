
def is_template_contained(image_a, template):
    for i in range(len(image_a) - len(template) + 1):
        for j in range(len(image_a[0]) - len(template[0]) + 1):
            if template == image_a[i:i + len(template), j:j + len(template)]:
                return True
    return False

def main():
    image_a_size, template_size = map(int, input().split())
    image_a = [input() for _ in range(image_a_size)]
    template = [input() for _ in range(template_size)]
    print("Yes") if is_template_contained(image_a, template) else print("No")

if __name__ == '__main__':
    main()

