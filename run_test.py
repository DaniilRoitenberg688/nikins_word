from test_logic import Test

from test_fnc import test_fnc

import sqlite3


def run_test(words: list, translations: list):
    test = Test(words, translations)

    for _ in range(len(test.words)):
        word, translation, changed_word = test.show_current()
        result = test_fnc(word, translation, changed_word)
        if not result:
            return
        if len(test.words) != 1:
            test.change_current()


if __name__ == '__main__':
    db = sqlite3.connect('words_db.sqlite')
    con = db.cursor()

    words = con.execute('SELECT word FROM words').fetchall()
    translations = con.execute('SELECT translation FROM words').fetchall()

    words = [i[0] for i in words]
    translations = [i[0] for i in translations]

    run_test(words, translations)