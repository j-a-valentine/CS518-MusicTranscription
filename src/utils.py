def remove_punctuation(text):
        punctuation_to_remove = "!?.,"
        translation_table = str.maketrans('', '', punctuation_to_remove)
        return text.translate(translation_table)