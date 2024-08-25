import time

import pygame

from constants import *
from test_logic import Test


def test_fnc(word, translation, changed_word, write_or_not: bool):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    font_size = 65
    if len(word) > 12:
        font_size = 45

    font = pygame.font.Font(None, font_size)

    font1 = pygame.font.Font(None, font_size)
    font2 = pygame.font.Font(None, font_size)

    continue_font = pygame.font.Font(None, 45)
    continue_text = continue_font.render('continue', True, WHITE)

    translation_text = font2.render(translation, True, BLACK)
    changed_word_text = font1.render(changed_word, True, BLACK)

    text = []

    running = True

    color = WHITE

    right = False

    while running:
        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.KEYDOWN:
                if event.key in possible_keys and not right:
                    text.append(possible_keys[event.key])
                if event.key == pygame.K_BACKSPACE and not right:
                    if text:
                        text.pop(-1)

                if right and event.key == pygame.K_RETURN:
                    running = False

                if not right and event.key == pygame.K_RETURN:
                    if ''.join(text) == word:
                        right = True
                        color = GREEN

                    else:
                        color = RED

            if event.type == pygame.MOUSEBUTTONDOWN:
                if right:
                    x, y = event.pos
                    if 225 <= x <= 375 and 325 <= y <= 375:
                        running = False

        pygame.draw.rect(screen, GREY, (50, 50, 300, 50))
        showing_text = font.render(''.join(text), True, BLACK)
        screen.blit(showing_text, (50, 50))
        if write_or_not:
            screen.blit(changed_word_text, (50, 150))
        screen.blit(translation_text, (50, 250))

        if right:
            pygame.draw.rect(screen, BLACK, (225, 325, 150, 50))
            screen.blit(continue_text, (235, 335))

        pygame.display.flip()

    return True


if __name__ == '__main__':
    test = Test(['cat'], ['кот'])
    test_fnc(*test.show_current())



