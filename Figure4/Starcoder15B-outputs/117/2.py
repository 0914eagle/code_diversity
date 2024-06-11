def select_words(s, n):
    
    # your code here
    return [word for word in s.split() if len(word) == n and word.isalpha()]


# + deletable=false editable=false nbgrader={"checksum": "761021230a26589913f404421963205a", "grade": true, "grade_id": "cell-954507110753e225", "locked": true, "points": 1, "schema_version": 1, "solution": false}
assert select_words("Mary had a little lamb", 4) == ["little"]
assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
assert select_words("simple white space", 2) == []
assert select_words("Hello world", 4) == ["world"]
assert select_words("Uncle sam", 3) == ["Uncle"]

# + [markdown] deletable=false editable=false nbgrader={"checksum": "1963843205124310860e26065355462a", "grade": false, "grade_id": "cell-936519333571358f", "locked": true, "schema_version": 1, "solution": false}
# ### Question 2
#
# Write a function `count_words(s)` that takes a string `s` as input and returns a dictionary that maps each word in `s` to the number of times it appears in `s`.
#
# For example:
#
# ```python
# count_words("Mary had a little lamb") == {"Mary": 1, "had": 1, "a": 1, "little": 1, "lamb": 1}
# count_words("Mary had a little lamb, little lamb, little lamb") == {"Mary": 1, "had": 1, "a": 1, "little": 3, "lamb": 3}
# count_words("Hello world") == {"Hello": 1, "world": 1}
#