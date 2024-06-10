
def get_template_length(template):
    return len(template)

def get_incomparable_strings(template1, template2):
    n = get_template_length(template1)
    if n != get_template_length(template2):
        raise ValueError("Template lengths do not match")
    
    count = 0
    for i in range(n):
        for j in range(n):
            if template1[i] > template2[j] and template1[j] < template2[i]:
                count += 1
    
    return count

def get_remainder(n):
    return n % 1000000007

def main():
    template1 = input()
    template2 = input()
    incomparable_strings = get_incomparable_strings(template1, template2)
    remainder = get_remainder(incomparable_strings)
    print(remainder)

if __name__ == '__main__':
    main()

