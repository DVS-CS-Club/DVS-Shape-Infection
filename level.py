import pygame as pyg
from typing import List

class Level:
    def __init__(self, boundaries: List[pyg.Rect], starting_pos: pyg.Vector2):
        self.boundaries = boundaries
        self.drawn_boundaries = boundaries
        self.starting_pos = starting_pos
    def update(self, screen, player_dx: int, player_dy: int):
        for boundary in self.drawn_boundaries:
            boundary.x += player_dx
            boundary.y += player_dy
            if boundary.colliderect(screen.get_rect()):
                pyg.draw.rect(screen, (255,165,0), boundary)
