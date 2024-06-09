
def get_translation(dutch_sentence, dictionary):
    correct_translations = []
    incorrect_translations = []
    for word in dutch_sentence.split():
        translations = dictionary[word]
        if len(translations) == 1:
            correct_translations.append(translations[0])
        else:
            for translation in translations:
                if translation[2] == "correct":
                    correct_translations.append(translation[1])
                else:
                    incorrect_translations.append(translation[1])
    return correct_translations, incorrect_translations

