import pygame
from constants import BALL_STEP


class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/ball.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.step = BALL_STEP
        self.was_fired = False
        self.fighter = fighter

    def fire(self):
        self.was_fired = True
        self.x = self.fighter.x + self.fighter.width / 2 - self.width / 2
        self.y = self.fighter.y - self.height

    def update_position(self, delta_time):
        if self.was_fired:
            self.y -= self.step * delta_time

    def is_out_of_screen(self):
        return self.y + self.height < 0

    def reset(self):
        self.was_fired = False

    def is_collision(self, alien):
        ball_center_x = self.x + self.width / 2
        ball_center_y = self.y + self.height / 2

        return (
                alien.x <= ball_center_x <= alien.x + alien.width
                and
                alien.y <= ball_center_y <= alien.y + alien.height
        )
