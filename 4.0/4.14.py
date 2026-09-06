import re

class TextHandler:

    def __init__(self):
        self.words = list()

    def add_words(self, text: str):
        self.words += re.split(r'\s+', text)

    def get_shortest_words(self):
        return list(
            filter(lambda x: len(x) == min(map(len, self.words)), self.words)
        )

    def get_longest_words(self):
        return list(
            filter(lambda x: len(x) == max(map(len, self.words)), self.words)
        )

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

# TEST_4:
texthandler = TextHandler()
texthandler.add_words('''Я помню чудное мгновенье
Передо мной явилась ты
Как мимолетное виденье
Как гений чистой красоты

В томленьях грусти безнадежной
В тревогах шумной суеты
Звучал мне долго голос нежный
И снились милые черты

Шли годы Бурь порыв мятежный
Рассеял прежние мечты
И я забыл твой голос нежный
Твои небесные черты

В глуши во мраке заточенья
Тянулись тихо дни мои
Без божества без вдохновенья
Без слез без жизни без любви

Душе настало пробужденье
И вот опять явилась ты
Как мимолетное виденье
Как гений чистой красоты

И сердце бьется в упоенье
И для него воскресли вновь
И божество и вдохновенье
И жизнь и слезы и любовь''')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())