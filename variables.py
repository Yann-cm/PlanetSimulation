LARGEUR = 1280
HAUTEUR = 650
G = 6.67430e-11  #constante gravitationel
AU = 1.496e11 #unité gravitationel , distance terre soleil
ECHELLE = 100/AU # 250 pixel est = a 1 unité gravitationel
TIMESTEP = 3600 

couleur = {
    "Terre": (12, 94, 238),
    "Soleil": (252, 215, 25),
    "Mars": (233, 53, 14),
    "Mercure": (169, 169, 169),
    "Vénus": (255, 223, 0),
    "Jupiter": (194, 124, 34),
    "Saturne": (210, 180, 140),
    "Uranus": (173, 216, 230),
    "Neptune": (72, 61, 139),
}


class screen :
    def __init__(self,screen) -> None:
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR
        self.screen = screen

