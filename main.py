import sqlite3

from constants import *
from run_test import run_test


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()

    font = pygame.font.Font(None, 100)

    text = font.render('start', True, WHITE)

    running = True

    db = sqlite3.connect('words_db.sqlite')
    con = db.cursor()

    words = con.execute('SELECT word FROM words').fetchall()
    translations = con.execute('SELECT translation FROM words').fetchall()

    words = [i[0] for i in words]
    translations = [i[0] for i in translations]

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 300 and 150 <= y <= 250:
                    run_test(words, translations)

        pygame.draw.rect(screen, BLACK, (100, 150, 200, 100))
        screen.blit(text, (120, 160))

        pygame.display.flip()

    con.close()


if __name__ == '__main__':
    main()
