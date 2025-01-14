LARGEUR = 1280
HAUTEUR = 650
G = 6.67430e-11  #constante gravitationel
AU = 1.496e11 #unité gravitationel , distance terre soleil
ECHELLE = 250/AU # 250 pixel est = a 1 unité gravitationel
TIMESTEP = 3600 

couleur = {
    "Terre" : (12,94,238),
    "Soleil" : (252,215,25),
    "Mars" : (233,53,14),

}

class screen :
    def __init__(self,screen) -> None:
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR
        self.screen = screen

