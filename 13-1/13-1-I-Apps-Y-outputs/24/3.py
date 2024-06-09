
def f1(s):
    # find the index of the first occurrence of 'A' in s
    start_index = s.find('A')
    # find the index of the last occurrence of 'Z' in s
    end_index = s.rfind('Z')
    # return the length of the substring
    return end_index - start_index + 1

