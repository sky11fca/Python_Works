def word_count(sentence):
    words=sentence.split()
    return len(words)

sentence="I have Python Exam"
print(word_count(sentence))