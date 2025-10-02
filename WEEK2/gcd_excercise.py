def gcd(a, b):
    while b:
        a, b=b, a%b
    return a


list_nr = [25, 125, 750, 225, 500]
result = list_nr[0]

for i in range(1, len(list_nr)):
    result = gcd(result, list_nr[i])

print(result)