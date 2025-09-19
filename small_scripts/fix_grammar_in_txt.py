def fix_grammar_in_txt():
    with open('../resources/text_files/snowwhite.txt') as r:
        text = r.read()

    sentences = text.split("\n")
    corrected_sentences = []

    for sentence in sentences:
        fixed_sentence = sentence.capitalize()
        corrected_sentences.append(fixed_sentence)

    corrected_text = ". \n".join(corrected_sentences)

    with open('../resources/text_files/snowwhite_corrected.txt', 'w') as w:
        w.write(corrected_text + ".")


if __name__ == "__main__":
    fix_grammar_in_txt()
