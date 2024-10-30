import pygame as pyg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.max_vel_x = 3
        self.max_vel_y = 3
    def update(self, screen):
        keys = pyg.key.get_pressed()
        if keys[pyg.K_LEFT] or keys[pyg.K_a]:
            self.vel_x -= 1
        if keys[pyg.K_RIGHT] or keys[pyg.K_d]:
            self.vel_x += 1
        if keys[pyg.K_DOWN] or keys[pyg.K_s]:
            self.vel_y += 1
        if keys[pyg.K_UP] or keys[pyg.K_w]:
            self.vel_y -= 1
        if self.vel_x > self.max_vel_x:
            self.vel_x = self.max_vel_x
        if self.vel_x < -self.max_vel_x:
            self.vel_x = -self.max_vel_x
        if self.vel_y > self.max_vel_y:
            self.vel_y = self.max_vel_y
        if self.vel_y < -self.max_vel_y:
            self.vel_y = -self.max_vel_y
        if not keys[pyg.K_LEFT] and not keys[pyg.K_a] and not keys[pyg.K_RIGHT] and not keys[pyg.K_d]:
            if self.vel_x > 0:
                self.vel_x -= 1
            if self.vel_x < 0:
                self.vel_x += 1
        if not keys[pyg.K_DOWN] and not keys[pyg.K_s] and not keys[pyg.K_UP] and not keys[pyg.K_w]:
            if self.vel_y > 0:
                self.vel_y -= 1
            if self.vel_y < 0:
                self.vel_y += 1
        # Check if we're moving diagonally, if so, reduce the speed
        if self.vel_x != 0 and self.vel_y != 0:
            self.vel_x /= 1.5
            self.vel_y /= 1.5
        self.x += self.vel_x
        self.y += self.vel_y
        pyg.draw.rect(screen, (0,255,255), (screen.get_width()//2-10, screen.get_height()//2-10, 20, 20))