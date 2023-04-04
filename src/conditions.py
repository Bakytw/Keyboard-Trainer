import datetime
import pygame
from constants import TIME
pygame.init()


class Start:
    def change_state(self, user):
        user.timer = pygame.time.get_ticks()
        user.word = ''
        user.printed = 0
        user.correct = 0
        return Write()


class Write:
    def change_state(self, user):
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        with open(f'records/{time}.txt', 'w+') as res:
            res.write(f'Time: {time}\n'
                      f'Count of mistakes: {user.printed - user.correct}\n'
                      f'Speed: {int(user.correct * (60.0 / TIME))} char/min\n')
        return Stats()


class Stats:
    def change_state(self, user):
        user.timer = pygame.time.get_ticks()
        user.word = ''
        user.printed = 0
        user.correct = 0
        return Write()
