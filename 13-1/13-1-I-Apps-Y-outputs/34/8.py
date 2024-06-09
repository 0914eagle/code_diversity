
def solve(s, k):
    n = len(s)
    for i in range(k):
        if 'a' in s:
            s = s.replace('a', '', 1)
        elif 'b' in s:
            s = s.replace('b', '', 1)
        elif 'c' in s:
            s = s.replace('c', '', 1)
        elif 'd' in s:
            s = s.replace('d', '', 1)
        elif 'e' in s:
            s = s.replace('e', '', 1)
        elif 'f' in s:
            s = s.replace('f', '', 1)
        elif 'g' in s:
            s = s.replace('g', '', 1)
        elif 'h' in s:
            s = s.replace('h', '', 1)
        elif 'i' in s:
            s = s.replace('i', '', 1)
        elif 'j' in s:
            s = s.replace('j', '', 1)
        elif 'k' in s:
            s = s.replace('k', '', 1)
        elif 'l' in s:
            s = s.replace('l', '', 1)
        elif 'm' in s:
            s = s.replace('m', '', 1)
        elif 'n' in s:
            s = s.replace('n', '', 1)
        elif 'o' in s:
            s = s.replace('o', '', 1)
        elif 'p' in s:
            s = s.replace('p', '', 1)
        elif 'q' in s:
            s = s.replace('q', '', 1)
        elif 'r' in s:
            s = s.replace('r', '', 1)
        elif 's' in s:
            s = s.replace('s', '', 1)
        elif 't' in s:
            s = s.replace('t', '', 1)
        elif 'u' in s:
            s = s.replace('u', '', 1)
        elif 'v' in s:
            s = s.replace('v', '', 1)
        elif 'w' in s:
            s = s.replace('w', '', 1)
        elif 'x' in s:
            s = s.replace('x', '', 1)
        elif 'y' in s:
            s = s.replace('y', '', 1)
        elif 'z' in s:
            s = s.replace('z', '', 1)
        else:
            break
    return s

