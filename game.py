# Example file showing a basic pygame "game loop"
import pygame
from fonction_globale import *
from planetes import Planete
from variables import *

# pygame setup
pygame.init()
surface = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Simulation du Système Solaire")

# Classe écran simplifiée
class Screen:
    def __init__(self, surface):
        self.surface = surface
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR

screen = Screen(surface)

def main():
    run = True
    clock = pygame.time.Clock()
    
    new_l = screen.largeur
    new_h = screen.hauteur

    TIME_UPDATE = TIMESTEP * 24  # 1 jour en secondes

    # Création des corps célestes
    soleil = Planete("Soleil", 1.989e30, 0, 0, 0, 0, TIME_UPDATE)
    mercure = Planete("Mercure", 3.301e23, 0.39 * AU, 0, 0, 47.87e3, TIME_UPDATE)
    venus = Planete("Vénus", 4.867e24, 0.72 * AU, 0, 0, 35.02e3, TIME_UPDATE)
    terre = Planete("Terre", 5.972e24, AU, 0, 0, 29.78e3, TIME_UPDATE)
    mars = Planete("Mars", 6.39e23, 1.524 * AU, 0, 0, 24.077e3, TIME_UPDATE)
    jupiter = Planete("Jupiter", 1.898e27, 5.203 * AU, 0, 0, 13.07e3, TIME_UPDATE)
    saturne = Planete("Saturne", 5.683e26, 9.537 * AU, 0, 0, 9.69e3, TIME_UPDATE)
    uranus = Planete("Uranus", 8.681e25, 19.191 * AU, 0, 0, 6.81e3, TIME_UPDATE)
    neptune = Planete("Neptune", 1.024e26, 30.07 * AU, 0, 0, 5.43e3, TIME_UPDATE)
    
    planetes = [soleil, mercure, venus, terre, mars, jupiter, saturne, uranus, neptune]

    while run:
        clock.tick(60)
        screen.surface.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    mouse_pos = event.pos
                    if test_vitesse0.collidepoint(mouse_pos):
                        TIME_UPDATE = TIMESTEP * 12   
                        for planete in planetes: 
                            planete.timestep = TIME_UPDATE
                    elif test_vitesse1.collidepoint(mouse_pos):
                        TIME_UPDATE = TIMESTEP * 24 
                        for planete in planetes: 
                            planete.timestep = TIME_UPDATE  
                    elif test_vitesse2.collidepoint(mouse_pos):
                        TIME_UPDATE = TIMESTEP * 48
                        for planete in planetes: 
                            planete.timestep = TIME_UPDATE  

        for planete in planetes:
            planete.update_position(planetes)
            planete.draw(screen.surface)
        
        test_vitesse0, test_vitesse1, test_vitesse2 = Vitesse(screen, LARGEUR)
        test_jour = Jour("365", screen, LARGEUR)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
