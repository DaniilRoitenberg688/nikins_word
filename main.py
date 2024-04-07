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
    text3 = font.render('Body', True, WHITE)

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
                if 100 < x < 300 and 10 < y < 80:
                    words = con.execute('SELECT word FROM animals_and_other').fetchall()
                    translations = con.execute('SELECT translation FROM animals_and_other').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                if 50 < x < 350 and 210 < y < 280:
                    words = con.execute('SELECT word FROM umoj').fetchall()
                    translations = con.execute('SELECT translation FROM umoj').fetchall()
                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, False)

                if 130 < x < 260 and 110 < y < 180:
                    words = con.execute('SELECT word FROM toys').fetchall()
                    translations = con.execute('SELECT translation FROM toys').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                if 130 < x < 270 and 300 < y < 370:
                    words = con.execute('SELECT word FROM body').fetchall()
                    translations = con.execute('SELECT translation FROM body').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

        pygame.draw.rect(screen, BLACK, (100, 10, 200, 70))
        screen.blit(text, (117, 25))

        pygame.draw.rect(screen, BLACK, (130, 110, 130, 70))
        screen.blit(text1, (148, 125))

        pygame.draw.rect(screen, BLACK, (50, 210, 300, 70))
        screen.blit(text2, (65, 225))

        pygame.draw.rect(screen, BLACK, (130, 300, 140, 70))
        screen.blit(text3, (147, 315))

        pygame.display.flip()

    con.close()


if __name__ == '__main__':
    main()
