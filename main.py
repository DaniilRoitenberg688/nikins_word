import sqlite3

from constants import *
from run_test import run_test


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()

    font = pygame.font.Font(None, 60)

    text = font.render('Animals', True, WHITE)
    text1 = font.render('Toys', True, WHITE)
    text2 = font.render('Multiplication', True, WHITE)

    running = True

    db = sqlite3.connect('words.db')
    con = db.cursor()

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 < x < 300 and 30 < y < 100:
                    words = con.execute('SELECT word FROM animals_and_other').fetchall()
                    translations = con.execute('SELECT translation FROM animals_and_other').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                if 50 < x < 350 and 300 < y < 370:
                    words = con.execute('SELECT word FROM umoj').fetchall()
                    translations = con.execute('SELECT translation FROM umoj').fetchall()
                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, False)

                if 130 < x < 260 and 160 < y < 210:
                    words = con.execute('SELECT word FROM toys').fetchall()
                    translations = con.execute('SELECT translation FROM toys').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

        pygame.draw.rect(screen, BLACK, (100, 30, 200, 70))
        screen.blit(text, (117, 45))

        pygame.draw.rect(screen, BLACK, (130, 160, 130, 70))
        screen.blit(text1, (148, 175))

        pygame.draw.rect(screen, BLACK, (50, 300, 300, 70))
        screen.blit(text2, (65, 315))

        pygame.display.flip()

    con.close()


if __name__ == '__main__':
    main()
