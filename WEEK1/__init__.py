import random

def digitSum(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10

    return sum


print("Sup Browskis")

languages = ["C", "C++", "C#", "Java", "Go", "Rust", "JS", "PHP", "Swift", "Python"]

n = random.randint(0, 1000000)

result = (n*3 + 0b10101 + 0xFF)*6
while result > 9:
    result = digitSum(result)

print("Willy-nilly, this Autumn I subjegate myself to " + languages[result])