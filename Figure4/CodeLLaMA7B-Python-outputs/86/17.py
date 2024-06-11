def anti_shuffle(s):
    
    if not s:
        return s
    words = s.split()
    return ' '.join(sorted(words, key=lambda x: ''.join(sorted(x))))


if __name__ == '__main__':
