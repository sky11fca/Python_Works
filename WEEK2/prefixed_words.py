x = "learning leasure lenstra linux"
y = "le"

words = x.split()
cnt = 0

for word in words:
    if word.startswith(y):
        cnt += 1

print(cnt)