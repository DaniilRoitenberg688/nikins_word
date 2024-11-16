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
    text4 = font.render('Weather', True, WHITE)
    text5 = font.render('New', True, WHITE)

    running = True

    db = sqlite3.connect('words.db')
    con = db.cursor()

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # animals
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 < x < 300 and 10 < y < 80:
                    words = con.execute('SELECT word FROM animals_and_other').fetchall()
                    translations = con.execute('SELECT translation FROM animals_and_other').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                # umnoj
                if 50 < x < 350 and 210 < y < 280:
                    words = con.execute('SELECT word FROM school').fetchall()
                    translations = con.execute('SELECT translation FROM school').fetchall()
                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                # toys
                if 15 < x < 145 and 110 < y < 180:
                    words = con.execute('SELECT word FROM toys').fetchall()
                    translations = con.execute('SELECT translation FROM toys').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                # weather
                if 170 < x < 395 and 110 < y < 180:
                    words = con.execute('SELECT word FROM weather').fetchall()
                    translations = con.execute('SELECT translation FROM weather').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                # body
                if 50 < x < 190 and 300 < y < 370:
                    words = con.execute('SELECT word FROM body').fetchall()
                    translations = con.execute('SELECT translation FROM body').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

                # new
                if 233 < x < 353 and 300 < y < 370:
                    words = con.execute('SELECT word FROM new').fetchall()
                    translations = con.execute('SELECT translation FROM new').fetchall()

                    words = [i[0] for i in words]
                    translations = [i[0] for i in translations]
                    run_test(words, translations, True)

        # animals
        pygame.draw.rect(screen, BLACK, (100, 10, 200, 70))
        screen.blit(text, (117, 25))

        # toys
        pygame.draw.rect(screen, BLACK, (15, 110, 130, 70))
        screen.blit(text1, (30, 125))

        # weather
        pygame.draw.rect(screen, BLACK, (170, 110, 215, 70))
        screen.blit(text4, (195, 125))

        # multiplications
        pygame.draw.rect(screen, BLACK, (50, 210, 300, 70))
        screen.blit(text2, (65, 225))

        # body
        pygame.draw.rect(screen, BLACK, (50, 300, 140, 70))
        screen.blit(text3, (67, 315))

        # new
        pygame.draw.rect(screen, BLACK, (233, 300, 120, 70))
        screen.blit(text5, (250, 315))




        pygame.display.flip()

    con.close()


if __name__ == '__main__':
    main()
