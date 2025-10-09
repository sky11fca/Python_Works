sample1 = "Linux is great, I love learning Linux"
sample2 = "Linux"

words = sample1.split()

cnt = 0

for word in words:
    if word == sample2:
       cnt+=1

print(f"Nr of appearances of string {sample2} is {cnt}")