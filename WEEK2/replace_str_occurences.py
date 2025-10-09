pattern="Linux"
replacement="Windows"
sample="Linux is great, I love Linux"

words = sample.split()
for i in range(len(words)):
    if words[i] == pattern:
        words[i] = replacement

print(" ".join(words))