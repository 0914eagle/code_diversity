
import re

def solve(n, labels):
    pink_buttons = 0
    for label in labels:
        if re.search("pink|rose", label, re.IGNORECASE):
            pink_buttons += 1
    if pink_buttons == 0:
        return "I must watch Star Wars with my daughter"
    else:
        return pink_buttons

