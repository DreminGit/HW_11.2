def big_words(input_word):
    """функция делает все слова заглавными"""
    return input_word.upper()



def capitalize_words(s):
    """СДЕЛАЛИ ФИКС БАГА (ИМИТАЦИЯ) функция сделает заглавной первую букву каждого слова"""
    words = s.split()
    capitalized_words = [word.capitalize()
for word in words]
    return ' '.join(capitalized_words)