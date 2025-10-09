sample = "UpperCaseCamel"
results = [sample[0].lower()]

for char in sample[1:]:
    if char.isupper():
        results.append("_")
        results.append(char.lower())
    else:
        results.append(char)

print(''.join(results))