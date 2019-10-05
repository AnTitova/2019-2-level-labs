"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
text = '''
Of course, when mastering a foreign language requires a good memory, logical thinking. 
However, knowing the language, reading and speaking in a foreign language is a feasible task. 
It is only necessary to approach this issue with all seriousness. 
It is proved that the ability to language — not the privilege of the elect. All children 
learn languages quickly and easily. Successfully studying a foreign language and in adolescence. 
This means that the earlier a person begins to learn a language, the better he will achieve.
'''
for_words = ('foreign', 'however', 'children', 'successfully')

def calculate_frequences(text: str) -> dict:
    dict_frequency = {}
    if type(text) != str:
        return dict_frequency
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.split()
    lst_words = []
    for w in text:
        clear_word = ''
        for s in w:
            if s.isalpha():
                clear_word += s
        if clear_word != '':
            lst_words.append(clear_word)
    for i in lst_words:
        dict_frequency [i] = lst_words.count(i)
    return dict_frequency


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    dict_new = {}
    if type(frequencies) == dict and type(stop_words) == tuple:
        for k, i in frequencies.items():
            if type(k) == str and k not in stop_words:
                dict_new[k] = i
    return dict_new


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    pop_words = ()
    if type(frequencies) == dict and type(top_n) == int:
        new_list = list(frequencies.items())
        new_list.sort(key=lambda n: n[1], reverse=True)
        if len(new_list) < top_n:
            top_n = len(new_list)
        for i in range(top_n):
            word_an = new_list[i][0]
            pop_words += (word_an,)
    return pop_words
