
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def find_balanced_group(s: str, start: int) -> str:
        count = 0
        end = start
        while end < len(s):
            if s[end] == '(':
                count += 1
            elif s[end] == ')':
                count -= 1
                if count == 0:
                    return s[start:end + 1]
            end += 1
        return ''

    result = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            group = find_balanced_group(paren_string, i)
            result.append(group)
            i += len(group)
        else:
            i += 1

    return result

if __name__ == "__main__":
    input_string = input().replace(" ", "")
    result = separate_paren_groups(input_string)
    print(result)
