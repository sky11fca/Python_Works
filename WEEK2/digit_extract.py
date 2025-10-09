def digit_extract(string):
    nr_strings = []

    for i in string:
        if i.isdigit():
            nr_strings.append(i)
    return ''.join(nr_strings)


sample1 = "An apple is 123 USD"
sample2 = "abc123abc"

print(digit_extract(sample1))
print(digit_extract(sample2))