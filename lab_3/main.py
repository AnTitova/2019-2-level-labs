"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word not in self.storage:
            if self.storage:
                identifier = max(self.storage.values()) + 1
            else:
                identifier = 1
            self.storage[word] = identifier
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if not isinstance(word, str) or word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, id_of: int) -> str:
        if not isinstance(id_of, int):
            return "UNK"
        for keys, values in self.storage.items():
            if id_of == values:
                return keys
        return "UNK"

    def from_corpus(self, corpus: tuple):
        if not isinstance(corpus, tuple):
            return {}
        example = WordStorage()
        for word in corpus:
            if word not in self.storage:
                self.storage[word] = example.put(word)
        return self.storage


class NGramTrie:
    def __init__(self, n):
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.size = n

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple) or sentence == ():
            return "ERROR"
        grams = []
        for i in range(len(sentence)):
            if i < len(sentence) - self.size:
                grams.append(sentence[i: i + self.size])
            elif i == len(sentence) - self.size:
                grams.append(sentence[i:])
        for gram in grams:
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
        return "OK"

    def calculate_log_probabilities(self):
        for element in self.gram_frequencies:
            numbers = []
            for keys, values in self.gram_frequencies.items():
                if element[: self.size - 1] == keys[: self.size - 1]:
                    numbers.append(values)
            prob = self.gram_frequencies[element] / sum(numbers)
            self.gram_log_probabilities[element] = math.log(prob)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) != self.size - 1 or prefix == ():
            return []
        sent = []
        sent.extend(list(prefix))
        list_n = []
        for gram in self.gram_log_probabilities:
            gram_1 = gram[:len(gram) - 1]
            list_n.append(gram_1)
        while prefix in list_n:
            prob_l = []
            for keys, values in self.gram_log_probabilities.items():
                if prefix == keys[:len(keys) - 1]:
                    prob_l.append((values, keys))
            prob_l.sort(reverse=True)
            sent.append(prob_l[0][1][-1])
            prefix = prob_l[0][1][1:]
        return sent



def encode(storage_instance, corpus) -> list:
    encoded_corp = []
    for sent in corpus:
        code_sent = []
        for word in sent:
            code_sent.append(word)
            encoded_corp.append(code_sent)
            word = storage_instance.get_id_of(word)
    return encoded_corp


def split_by_sentence(text: str) -> list:
    sentences = []
    if not isinstance(text, str) or text == '' or '.' not in text:
        return sentences
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace('?', '.')
    text = text.replace('!', '.')
    text = text.split('. ')
    for sentence in text:
        clear_sentence = ''
        for sym in sentence:
            if sym.isalpha() or sym == ' ':
                clear_sentence += sym
        if clear_sentence:
            sent = ['<s>']
            sent.extend(clear_sentence.split())
            sent.append('</s>')
            sentences.append(sent)
    return sentences
