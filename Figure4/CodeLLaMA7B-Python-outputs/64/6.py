FIX = 

def vowels_count(s):
    
    vowels = 'aeiou'
    return sum(s.count(v) for v in vowels)


if __name__ == "__main__":
    import doctest
   