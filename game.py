# Example file showing a basic pygame "game loop"
import pygame
from fonction_globale import *
from planetes import Planete
from variables import *

# pygame setup
pygame.init()
surface = pygame.display.set_mode((LARGEUR, HAUTEUR))
screen = screen(surface)

pygame.display.set_caption("Simulation du Système Solaire")



def main():
    run = True
    clock = pygame.time.Clock()
    
    TIME_UPDATE = TIMESTEP * 24 # 1 jour en secondes

    # Création des corps célestes
    soleil = Planete("Soleil", 1.989e30, 0, 0, 0, 0,TIME_UPDATE)
    terre = Planete("Terre", 5.972e24, AU, 0, 0, 29.783e3,TIME_UPDATE)
    mars = Planete("Mars", 6.39e23, 1.524 * AU, 0, 0, 24.077e3,TIME_UPDATE)
    planetes = [soleil, terre, mars]



    while run:
        clock.tick(60)
        screen.screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN  :
                if event.key == pygame.K_e :
                    run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    mouse_pos = event.pos
                
                    
                    if test_vitesse0.collidepoint(mouse_pos) :
                        TIME_UPDATE = TIMESTEP * 12   
                        for planete in planetes : 
                            planete.timestep = TIME_UPDATE  

                    elif test_vitesse1.collidepoint(mouse_pos) :
                        TIME_UPDATE = TIMESTEP * 24 
                        for planete in planetes : 
                            planete.timestep = TIME_UPDATE  
                    
                    elif test_vitesse2.collidepoint(mouse_pos) :
                        TIME_UPDATE = TIMESTEP * 48
                        for planete in planetes : 
                            planete.timestep = TIME_UPDATE  
        
    
        for planete in planetes :
            planete.update_position(planetes)
            planete.draw(screen.screen)
        
        test_vitesse0,test_vitesse1,test_vitesse2 = Vitesse(screen,LARGEUR)
        test_jour = Jour("365",screen,LARGEUR)



        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


