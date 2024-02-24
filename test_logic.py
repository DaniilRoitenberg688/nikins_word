from random import randint, shuffle


class Test:
    def __init__(self, words: list, translations: list):
        self.words = words
        self.translations = translations
        self.current = randint(0, len(words) - 1)

    def change_current(self):
        self.words.pop(self.current)
        self.translations.pop(self.current)
        self.current = randint(0, len(self.words) - 1)

    def show_current(self):
        changed = list(self.words[self.current])
        while changed == list(self.words[self.current]):
            shuffle(changed)
        return self.words[self.current], self.translations[self.current], ''.join(changed)


if __name__ == '__main__':
    test = Test(['dog', 'cat'], ['собака', 'кот'])
    for _ in range(len(test.words)):
        word, translation, changed_word = test.show_current()
        print(translation)
        print(changed_word)
        answer = input()
        while word != answer:
            print(translation)
            print(changed_word)
            answer = input()

        if len(test.words) != 1:
            test.change_current()
