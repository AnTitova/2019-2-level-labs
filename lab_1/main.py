"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
TEXT = '''
Of course, when mastering a foreign language requires a good memory, logical thinking. 
However, knowing the language, reading and speaking in a foreign language is a feasible task. 
It is only necessary to approach this issue with all seriousness. 
It is proved that the ability to language — not the privilege of the elect. All children 
learn languages quickly and easily. Successfully studying a foreign language and in adolescence. 
This means that the earlier a person begins to learn a language, the better he will achieve.
'''
FOR_WORDS = ('foreign', 'however', 'children', 'successfully')


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    dict_frequency = {}
    if not isinstance(text, str): # change type - isinstance
        return dict_frequency
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.split()
    lst_words = []
    for wor in text:
        clear_word = ''
        for sym in wor:
            if sym.isalpha():
                clear_word += sym
        if clear_word != '':
            lst_words.append(clear_word)
    for i in lst_words:
        dict_frequency[i] = lst_words.count(i)
    return dict_frequency


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    dict_new = {}
    if isinstance(frequencies, dict) and isinstance(stop_words, tuple): #type - isinstance()
        for k, i in frequencies.items():
            if isinstance(k, str) and k not in stop_words:
                dict_new[k] = i
    return dict_new


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    pop_words = ()
    if isinstance(frequencies, dict) and isinstance(top_n, int):
        new_list = list(frequencies.items())
        new_list.sort(key=lambda n: n[1], reverse=True)
        if len(new_list) < top_n:
            top_n = len(new_list)
        for i in range(top_n):
            word_an = new_list[i][0]
            pop_words += (word_an,)
    return pop_words
