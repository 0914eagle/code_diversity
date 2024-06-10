
def get_template_permutations(template):
    permutations = []
    for i in range(len(template)):
        if template[i] == '?':
            permutations.extend([template[:i] + str(j) + template[i+1:] for j in range(10)])
        else:
            permutations.append(template)
    return permutations

def are_strings_incomparable(s, w):
    for i in range(len(s)):
        if s[i] > w[i] and s[i+1] < w[i+1]:
            return True
    return False

def count_incomparable_templates(template1, template2):
    permutations1 = get_template_permutations(template1)
    permutations2 = get_template_permutations(template2)
    count = 0
    for p1 in permutations1:
        for p2 in permutations2:
            if are_strings_incomparable(p1, p2):
                count += 1
    return count

def main():
    n = int(input())
    template1 = input()
    template2 = input()
    count = count_incomparable_templates(template1, template2)
    print(count % 1000000007)

if __name__ == '__main__':
    main()

