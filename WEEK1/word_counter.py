def word_counter(text):
    words=sample.split()
    return len(words)

sample="I have Python Exam" # should be 4

print(word_counter(sample))