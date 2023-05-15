import datetime
import pygame
from constants import TIME
pygame.init()


class Start:
    '''Начальная позиция'''

    def change_state(self, user):
        '''Начало тренировки'''
        user.timer = pygame.time.get_ticks()
        user.word = ''
        user.printed = 0
        user.correct = 0
        return Write()


class Write:
    '''Состояние печатания'''

    def change_state(self, user):
        '''Возвращение статистики'''
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        with open(f'records/{time}.txt', 'w+') as res:
            res.write(f'Time: {time}\n'
                      f'Count of mistakes: {user.printed - user.correct}\n'
                      f'Speed: {int(user.correct * (60.0 / TIME))} char/min\n')
        return Stats()


class Stats:
    '''Состояние статистики'''

    def change_state(self, user):
        '''Начало тренировки'''
        user.timer = pygame.time.get_ticks()
        user.word = ''
        user.printed = 0
        user.correct = 0
        return Write()
