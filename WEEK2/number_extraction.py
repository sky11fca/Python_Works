NUMBERS="0123456789"

def extract_numbers(text):
    result=[]
    for char in text:
        if char in NUMBERS:
            result.append(char)

    return ''.join(result)


sample="An apple is 123 USD"

print(extract_numbers(sample))

