import pygame
from constants import BLACK, RED
pygame.init()


class Button:
    '''Иконка кнопки, при нажатии начать игру'''

    def create_button(self, screen, x, y, length, height):
        '''Создание кнопки'''
        pygame.draw.rect(screen, RED, (x, y, length, height), 0)
        screen = self.write_text(screen, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return screen

    def write_text(self, screen, length, height, x, y):
        '''Текст на кнопке'''
        text_screen = pygame.font.SysFont(
            'courier', length // len('Start')).render('Start', True, BLACK)
        text_rect = text_screen.get_rect(
            center=(x + length / 2, y + height / 2))
        screen.blit(text_screen, text_rect)
        return screen

    def pressed(self, mouse):
        '''Фиксация нажатия на кнопку'''
        return self.rect.bottomright[0] > mouse[0] > self.rect.topleft[0] and self.rect.bottomright[1] > mouse[1] > self.rect.topleft[1]
