# Cout the Vowel from the given word
# Input_string = " Hello, Wolrd"
# Vowel = a,e,i,o,u


input_string = " Hello, Wolrd"

vowels = "aeiou"
vowels_count = 0

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1

print(vowels_count)


