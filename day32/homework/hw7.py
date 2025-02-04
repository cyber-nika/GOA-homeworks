def paragraph_to_sentences(paragraph):
    return [sentence.strip() for sentence in paragraph.split(".") if sentence.strip()]
