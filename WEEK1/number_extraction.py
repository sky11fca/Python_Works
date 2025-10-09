def extract_numbers(text):
    result=[]
    for char in text:
        if char.isdigit():
            result.append(char)

    return ''.join(result)


sample="An apple is 123 USD"

print(extract_numbers(sample))

