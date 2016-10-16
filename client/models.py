import pygame

class Player:
    def __init__(self, name, index):
        self.name = name
        self.score = 0
        self.index = index
        self.sound = pygame.mixer.Sound('../resources/sounds/buzzer-' + str(index) + '.wav')
        self.buzzer = None

    def add_score(self, points):
        self.score += points
