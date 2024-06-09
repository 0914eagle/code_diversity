
import re

def solve(n, colors):
    pink_buttons = 0
    for color in colors:
        if re.search("pink|rose", color, re.IGNORECASE):
            pink_buttons += 1
    if pink_buttons == 0:
        return "I must watch Star Wars with my daughter"
    else:
        return pink_buttons

