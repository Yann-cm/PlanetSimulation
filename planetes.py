import math
import pygame

from variables import *


class Planete :
    def __init__(self,nom,mass,x,y,vx,vy,timestep) -> None:
        self.nom = nom
        self.mass = mass
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.color = couleur[nom]
        self.timestep = timestep
    
    def attraction(self,other) :
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2) #calcul de la distance entre la planete A et B
        force = G * (self.mass * other.mass)/ distance**2 #Calcul de la force gravitationell
        theta = math.atan2(dy, dx) #calcul de l'angle de direction
        fx = math.cos(theta) * force #decomposition de la force en valeur X et Y
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

        # Mise à jour de la vitesse
        self.vx += fx / self.mass * self.timestep
        self.vy += fy / self.mass * self.timestep

        # Mise à jour de la position
        self.x += self.vx * self.timestep
        self.y += self.vy * self.timestep

    def draw(self,screen) :
        x = self.x * ECHELLE + LARGEUR / 2
        y = self.y * ECHELLE + HAUTEUR / 2
        pygame.draw.circle(screen, self.color, (int(x), int(y)), 5)