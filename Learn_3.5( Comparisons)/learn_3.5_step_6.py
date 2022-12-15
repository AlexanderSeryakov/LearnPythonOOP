""" Ваша задача написать программу поиска слова в строке. Задача усложняется тем, что слово должно определяться в
разных его формах. Например, слово:

программирование

может иметь следующие формы:

программирование, программированию, программированием, программировании, программирования, программированиям,
программированиями, программированиях

Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:

mw = Morph(word1, word2, ..., wordN)
где word1, word2, ..., wordN - возможные формы слова.

В классе Morph реализовать методы:

add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
get_words(self) - получение кортежа форм слов.

Также с объектами класса Morph должны выполняться следующие операторы сравнения:

mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
И аналогичная пара сравнений:

"word" == mw1
"word" != mw1
После создания класса Morph, формируется список dict_words из объектов этого класса, для следующих слов с их словоформами:

- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях

Затем, прочитайте строку из входного потока командой:

text = input()
Найдите все вхождения слов из списка dict_words (используя операторы сравнения) в строке text (без учета регистра,
знаков пунктуаций и их словоформы). Выведите на экран полученное число.

Sample Input:

Мы будем устанавливать связь завтра днем.
Sample Output:

2"""


class Morph:
    def __init__(self, *args):
        self.words = [x.lower() for x in args]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return any(other.lower() == word for word in self.words)


words = """- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""
dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in words.splitlines()]

text = input()

res = sum(word == morph for word in text.strip('.').split() for morph in dict_words)
print(res)
