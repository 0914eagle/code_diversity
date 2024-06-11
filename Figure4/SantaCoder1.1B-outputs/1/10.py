from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    paren_groups = []
    paren_group = []
    for char in paren_string:
        if char == "(":
            paren_group.append(char)
        elif char == ")":
            if len(paren_group) > 0:
                paren_groups.append("".join(paren_group))
                paren_group = []
            else:
                paren_groups.append(char)
        else:
            paren_group.append(char)
    if len(paren_group) > 0:
        paren_groups.append("".join(paren_group))
    return paren_groups


