word_1 = 'cookies'
word_2 = 'sometimes'


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if not isinstance(num_rows, int) or not isinstance(num_cols, int):
        return []
    else:
       new_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]
    return new_matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not isinstance(edit_matrix, tuple) or len(edit_matrix) == 0:
        return []
    edit_matrix = list(edit_matrix)
    if edit_matrix.count([]):
        return edit_matrix
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return edit_matrix
    for el in range(len(edit_matrix[0])):
        if el != 0:
            edit_matrix[0][el] = edit_matrix[0][el-1] + add_weight
    for col in range(len(edit_matrix)):
        if col != 0:
            edit_matrix[col][0] = edit_matrix[col-1][0] + remove_weight
    return edit_matrix


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if not isinstance (edit_matrix, tuple):
        return []
    edit_matrix = list(edit_matrix)
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return edit_matrix
    if not isinstance(original_word, str) or not isinstance(target_word, str) or original_word == '' or \
            target_word == '':
        return edit_matrix
    original_word = ' ' + original_word
    target_word = ' ' + target_word
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
            m1 = edit_matrix[i-1][j] + remove_weight
            m2 = edit_matrix[i][j-1] + add_weight
            m3 = edit_matrix[i-1][j-1]
            if original_word[i] != target_word[j]:
                m3 += substitute_weight
            minimum = minimum_value((m1, m2, m3))
            edit_matrix[i][j] = minimum
    return edit_matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if not isinstance(original_word, str) or not isinstance(target_word, str) or not isinstance(add_weight, int)\
            or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
       return -1
    new_matrix = generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)
    new_matrix_1 = initialize_edit_matrix(tuple(new_matrix), add_weight, remove_weight)
    new_matrix_2 = fill_edit_matrix(tuple(new_matrix_1), add_weight, remove_weight, substitute_weight, original_word,
                                    target_word)
    last_el = new_matrix_2[-1][-1]
    return last_el


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    with open(path_to_file, 'w') as new_file:
        for row in edit_matrix:
            for el in row:
                el = str(el)
                new_file.write(el + ',')
            new_file.write('\n')


def load_from_csv(path_to_file: str) -> list:
    with open(path_to_file) as new_file:
        new_matrix = []
        for line in new_file:
            new_str = []
            for el in line:
                if el.isdigit():
                    new_str.append(int(el))
            new_matrix.append(new_str)
    return new_matrix
