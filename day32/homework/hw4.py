def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return " ".join(words)
