import pygame

class creator:
    def __init__(self):
        self.buttons = []
        self.callbacks_ = []
        self.currindex = 0

    def add_option(self, option, callback, font):
        self.buttons.append(font.render(option, True, (255, 255, 255)))
        self.callbacks_.append(callback)

    def switch_point(self, direction):
        self.currindex = max(
            0, min(self.currindex + direction, len(self.buttons) - 1))

    def select(self):
        if self.callbacks_[self.currindex] != False:
            self.callbacks_[self.currindex]()
        else:
            pass

    def draw(self, srf, x, y, option_y):
        for i, option in enumerate(self.buttons):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y)
            if i == self.currindex:
                pygame.draw.rect(srf, (0, 100, 0), option_rect)
            srf.blit(option, option_rect)
    
    def clearing(self):
        self.buttons = []
        self.callbacks_ = []
        self.currindex = 0