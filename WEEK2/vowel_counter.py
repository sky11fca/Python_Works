VOWELS = "aeiouAEIOU"
counter = 0

sample_string = "Python is GRRRRRRRREEEEEEAAAAATTT)"


for char in sample_string:
    if char in VOWELS:
        counter += 1

print(f"Nr of vowels is: {counter}" )