def gcd(a, b):
    while b:
        a, b=b, a%b
    return a


#
numbers = []

#receiving the input numbers from the console
input_numbers = str(input())

#Converting the input string into a list of numbers
numbers_str = input_numbers.split()
for number in numbers_str:
  numbers.append(int(number))

result = numbers[0]

if len(numbers) != 1:
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])

print(result)