def gcd(a, b):
    while b:
        a, b=b, a%b
    return a


#
numbers = []
input_numbers = str(input())

numbers_str = input_numbers.split()

for number in numbers_str:
  numbers.append(int(number))

result = numbers[0]

for i in range(1, len(numbers)):
    result = gcd(result, numbers[i])

print(result)