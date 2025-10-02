sample1 = "Linux"
sample2 = "Linux is great! I love learning Linux" # Must be 2 occurences

list_of_words = sample2.split()
counter = 0

for word in list_of_words:
    if sample1 == word:
        counter +=1

print(f"nr of appearances of string {sample1} is {counter}")