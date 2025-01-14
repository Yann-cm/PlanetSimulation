import math
import pygame
from variables import *

class Planete:
    def __init__(self, nom, mass, x, y, vx, vy, timestep):
        self.nom = nom
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = couleur[nom]
        self.timestep = timestep
    
    def attraction(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        force = G * (self.mass * other.mass) / distance**2
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * force
        fy = math.sin(theta) * force
        return fx, fy
    
    def update_position(self, bodies):
        fx = fy = 0
        for body in bodies:
            if self == body:
                continue
            temp_fx, temp_fy = self.attraction(body)
            fx += temp_fx
            fy += temp_fy

        self.vx += fx / self.mass * self.timestep
        self.vy += fy / self.mass * self.timestep

        self.x += self.vx * self.timestep
        self.y += self.vy * self.timestep

    def draw(self, screen):
        x = self.x * ECHELLE + LARGEUR / 2
        y = self.y * ECHELLE + HAUTEUR / 2
        pygame.draw.circle(screen, self.color, (int(x), int(y)), 5)
