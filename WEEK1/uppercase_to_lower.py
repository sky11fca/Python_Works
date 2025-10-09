sample="UpperCaseCamel" # should return upper_case_camel

result=[sample[0].lower()]

for char in sample[1:]:
    if char.isupper() :
        result.append("_")
        result.append(char.lower())
    else:
        result.append(char)

print(''.join(result))

