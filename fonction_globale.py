import pygame


def texte(string,couleur,coo,screen) :
    police = pygame.font.SysFont("monospace",15)
    image_texte = police.render (string,1,couleur)
    screen.blit(image_texte, coo)



def Vitesse(screen,largeur ):
    couleur = "white"
    variable_comune = largeur/32

    #X0.5*
    texte("X0.5", couleur, (0, screen.hauteur - 25), screen.screen)
    Vitesse0 = pygame.draw.rect(screen.screen, couleur, pygame.Rect(0, screen.hauteur - variable_comune, variable_comune, variable_comune), 2)

    #X1
    texte("X1", couleur, (variable_comune+10, screen.hauteur - 25), screen.screen)
    Vitesse1 = pygame.draw.rect(screen.screen, couleur, pygame.Rect(variable_comune, screen.hauteur - variable_comune, variable_comune, variable_comune), 2)

    #X2
    texte("X2", couleur, (variable_comune*2+10, screen.hauteur - 25), screen.screen)
    Vitesse2 = pygame.draw.rect(screen.screen, couleur, pygame.Rect(variable_comune*2, screen.hauteur - variable_comune, variable_comune, variable_comune), 2)
    
    return Vitesse0, Vitesse1,Vitesse2

def Jour(string, screen,largeur ):
    couleur = "white"
    variable_comune = largeur/32

    #Nombre de jour
    texte(string, couleur, (screen.largeur-5, screen.hauteur - 25), screen.screen)
    Jour = pygame.draw.rect(screen.screen, couleur, pygame.Rect(screen.largeur-variable_comune*2, screen.hauteur - variable_comune*2, screen.largeur, screen.hauteur), 2)
  
    return Jour