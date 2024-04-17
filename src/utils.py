import Levenshtein

def remove_punctuation(text):
        punctuation_to_remove = "!?.,"
        translation_table = str.maketrans('', '', punctuation_to_remove)
        return text.translate(translation_table)

def get_similarity_score(sentence1, sentence2):
        distance = Levenshtein.distance(sentence1, sentence2)
        max_distance = max(len(sentence1), len(sentence2))
        if max_distance == 0:
                return 1
        return 1 - (distance / max_distance)