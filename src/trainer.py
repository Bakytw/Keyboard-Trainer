from button import Button
from conditions import Start, Stats, Write
import constants as c
import pygame
pygame.init()


class KeyboardTrainer:
    '''Реализация клавиатурного тренажера'''

    def __init__(self):
        '''Инициализация полей'''
        pygame.display.set_caption('Keyboard Trainer')
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self.timer = pygame.time.get_ticks()
        self.state = Start()
        self.starting = Button()
        self.printed = 0
        self.correct = 0
        self.index = 0
        self.word = ''
        self.dictionary = []
        with open('input.txt', 'r') as input:
            for line in input:
                for word in line.split():
                    self.dictionary.append(word)

    def start(self):
        '''Начальный экран'''
        self.screen.blit(c.STANDART_FONT.render(
            'Go!', True, c.BLACK), c.START_POS)
        self.starting.create_button(self.screen, *c.BUTTON_POS, *c.BUTTON_SIZE)

    def write(self):
        '''Экран тренировки'''
        if self.is_finished():
            temp = ''
        else:
            temp = self.dictionary[self.index]
        self.screen.blit(c.STANDART_FONT.render(
            f'Time left: {c.TIME - (pygame.time.get_ticks() - self.timer) // 1000} sec', True, c.BLACK), c.TIME_POS)
        self.screen.blit(c.STANDART_FONT.render(
            temp, True, c.BLACK), c.WORD_POS)
        self.screen.blit(c.STANDART_FONT.render(
            self.word, True, c.BLACK), c.USER_POS)
        if pygame.time.get_ticks() - self.timer >= 1000 * c.TIME:
            self.state = self.state.change_state(self)

    def stats(self):
        '''Экран статистики'''
        self.screen.blit(c.STAT_FONT.render(
            'Statistics', True, c.BLACK), c.STAT_POS)
        self.screen.blit(c.INFO_FONT.render(
            f'Count of mistakes: {self.printed - self.correct}', True, c.BLACK), c.ERROR_POS)
        self.screen.blit(c.INFO_FONT.render(
            f'Speed: {int(self.correct * (60.0 / c.TIME))} char/min', True, c.BLACK), c.SPEED_POS)
        self.starting.create_button(
            self.screen, *c.STAT_BUTTON_POS, *c.BUTTON_SIZE)

    def is_finished(self):
        '''Фиксация концовки печатания'''
        return self.index >= len(self.dictionary)

    def event_loop(self):
        '''Процесс игры'''
        running = True
        while running:
            pygame.time.Clock().tick(c.FPS)
            self.screen.fill(c.WHITE)
            if type(self.state) == Start:
                self.start()
            elif type(self.state) == Write:
                self.write()
            elif type(self.state) == Stats:
                self.stats()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif type(self.state) != Write and event.type == pygame.MOUSEBUTTONDOWN:
                    if self.starting.pressed(pygame.mouse.get_pos()):
                        self.state = self.state.change_state(self)
                elif type(self.state) == Write and event.type == pygame.KEYDOWN:
                    if self.is_finished():
                        continue
                    self.printed += 1
                    if chr(event.key) == self.dictionary[self.index][len(self.word)]:
                        self.correct += 1
                        self.word += chr(event.key)
                    if len(self.word) >= len(self.dictionary[self.index]):
                        self.index = (self.index + 1) % len(self.dictionary)
                        self.word = ''
            if type(self.state) == Write and self.is_finished():
                self.state = self.state.change_state(self)
            pygame.display.update()
