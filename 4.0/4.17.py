from copy import deepcopy


class Wordplay:

    def __init__(self, words=None):

        self.words = deepcopy(words) if words else list()


    def add_word(self, word: str):

        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return list(filter(lambda x: len(x) == n, self.words))


    def only(self, *args):

        new = list()
        for word in self.words:
            if set(word).issubset(set(args)):
                new.append(word)
        return new


    def avoid(self, *args):

        new = list()
        for word in self.words:
            if set(word).isdisjoint(set(args)):
                new.append(word)
        return new




# # TEST_1:
# wordplay = Wordplay()

# print(wordplay.words_with_length(1))
# print(wordplay.only('a', 'b', 'c'))
# print(wordplay.avoid('a', 'b', 'c'))

# # TEST_2:
# wordplay = Wordplay()

# print(wordplay.words)
# wordplay.add_word('bee')
# wordplay.add_word('geek')
# print(wordplay.words)

# # TEST_3:
# wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

# wordplay.add_word('python')
# print(wordplay.words_with_length(4))

# # TEST_4:
# wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

# print(wordplay.only('o', 't'))

# # TEST_5:
# wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

# print(wordplay.avoid('a', 'b', 'c'))

# # TEST_6:
# wordplay = Wordplay()
# print(wordplay.words)

# # TEST_7:
# wordplay = Wordplay(['Тьюринг', 'Торвальдс', 'Россум', 'Гейтс', 'Гамильтон', 'Бэкус', 'Кнут'])

# print(wordplay.words_with_length(6))
# print(wordplay.avoid('ь'))

# TEST_8:
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)

# # TEST_9:
# wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

# print(wordplay.words)
# wordplay.add_word('stepik')
# wordplay.add_word('bee')
# wordplay.add_word('geek')
# print(wordplay.words)