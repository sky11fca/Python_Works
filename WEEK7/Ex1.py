def more_than_n_words(sentence, n):
    word_list = sentence.split()
    words_at_least_n = [word for word in word_list if len(word) >= n]
    return words_at_least_n

print(more_than_n_words("How are you today?", 4))