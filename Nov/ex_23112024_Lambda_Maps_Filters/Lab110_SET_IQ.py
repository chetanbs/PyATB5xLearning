# Find the first non-repeating characteer in a string using sets
# swiss - s - x, w -answer

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss"))
print(first_non_repeating("pepper"))
print(first_non_repeating("DADA"))
