import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if not isinstance(texts, list):
        return []
    lst_words = []
    for tex in texts:
        if not isinstance(tex, str):
            continue
        text = tex.replace('<br />', ' ')
        n_text = ''
        for symbol in text:
            if symbol.isalpha() or symbol == ' ':
                n_text += symbol.lower()
        lst_words.append(n_text.split())
    return lst_words

class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if self.corpus:
            for text_1 in self.corpus:
                tf_values = {}
                if text_1:
                    text_len = len(text_1)
                    for word in text_1:
                        if not isinstance(word, str):
                            text_len -= 1
                    for word in text_1:
                        if isinstance(word, str) and word not in tf_values:
                            count_word = text_1.count(word)
                            tf_values[word] = count_word / text_len
                    self.tf_values += [tf_values]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            for text_1 in self.corpus:
                if not text_1:
                    continue
                new_corp = []
                for word in text_1:
                    if isinstance(word, str) and word not in new_corp:
                        new_corp += [word]
                count_wor = {}
                for word in new_corp:
                    count_word = 0
                    for text_2 in self.corpus:
                        if not text_2 or word in text_2:
                            count_word += 1
                    count_wor[word] = count_word
                    if count_wor.get(word) != 0:
                        len_c = len(self.corpus)
                        self.idf_values[word] = math.log(len_c / count_wor.get(word))
            return self.idf_values

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return
        for text_1 in self.tf_values:
            tf_idf_text = {}
            for word, value in text_1.items():
                tf_idf_text[word] = value * self.idf_values[word]
            self.tf_idf_values.append(tf_idf_text)

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dict = self.tf_idf_values[document_index]
        if not word in tf_idf_dict:
            return ()
        list_tf_idf = sorted(tf_idf_dict, key=tf_idf_dict.__getitem__, reverse=True)
        return tf_idf_dict.get(word.lower()), list_tf_idf.index(word.lower())

if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))

