import pygame
import numpy as np 

# Initialiser Pygame
pygame.init()
pygame.display.init()

# Dimensions de la grille
n_lignes = 140
n_colonnes = 300
taille_case = 6  # Taille de chaque case
frame = 0        # nb de frames
tot_viv = int(0)      # nb de cellules vivantes

# Taille de la fenêtre
largeur_fenetre = n_colonnes * taille_case
hauteur_fenetre = n_lignes * taille_case + 50  # Espace supplémentaire pour le bouton
pygame.display.set_caption("Jeu de la vie")
pygame.display.set_icon(pygame.image.load('logo.png'))

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Initialiser la grille avec des valeurs aléatoires de True/False
cellule = np.random.choice([True, False], (n_lignes, n_colonnes))

# Créer un rectangle pour le bouton
bouton_rect = pygame.Rect(10, hauteur_fenetre - 40, 200, 30)
bouton_stop = pygame.Rect(240, hauteur_fenetre - 40, 200, 30)
bouton_quit = pygame.Rect(470, hauteur_fenetre - 40, 200, 30)
bouton_frame = pygame.Rect(700, hauteur_fenetre - 40, 200, 30)
bouton_cell = pygame.Rect(930, hauteur_fenetre - 40, 200, 30)
bouton_clear = pygame.Rect(1160, hauteur_fenetre - 40, 200, 30)
bouton_rdm = pygame.Rect(1390, hauteur_fenetre - 40, 200, 30)

# Fonction pour appliquer les règles de Conway sans toucher aux bords
def appliquer_regles():
    # Créer une copie de la grille pour éviter de modifier la grille d'origine pendant les calculs
    nouvelle_cellule = np.copy(cellule)

    for i in range(1, n_lignes - 1):
        for j in range(1, n_colonnes - 1):
            # Compter les voisins actifs autour de la cellule (i, j)
            voisins_actifs = sum([
                cellule[i - 1, j - 1], cellule[i - 1, j], cellule[i - 1, j + 1],
                cellule[i, j - 1],                    cellule[i, j + 1],
                cellule[i + 1, j - 1], cellule[i + 1, j], cellule[i + 1, j + 1]
            ])
            
            # Appliquer les règles de Conway
            if cellule[i, j]:  # Si la cellule est active
                nouvelle_cellule[i, j] = voisins_actifs in [2, 3]
            else:  # Si la cellule est inactive
                nouvelle_cellule[i, j] = voisins_actifs == 3


    # Mettre à jour la grille avec les nouveaux états, en évitant de modifier les bords
    cellule[1:-1, 1:-1] = nouvelle_cellule[1:-1, 1:-1]
    # Forcer les bords à False
    cellule[0, :] = False           # Bord supérieur
    cellule[-1, :] = False          # Bord inférieur
    cellule[:, 0] = False           # Bord gauche
    cellule[:, -1] = False          # Bord droit
    
def erase_cell():
    # Créer une copie de la grille pour éviter de modifier la grille d'origine pendant les calculs
    nouvelle_cellule = np.copy(cellule)
    for i in range(1, n_lignes - 1):
        for j in range(1, n_colonnes - 1):            
            if cellule[i, j]:
                nouvelle_cellule[i, j] = False
            else:  # Si la cellule est inactive
                nouvelle_cellule[i, j] = False
    # Mettre à jour la grille avec les nouveaux états, en évitant de modifier les bords
    cellule[1:-1, 1:-1] = nouvelle_cellule[1:-1, 1:-1]

# Boucle principale
en_cours = True
z = False

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
            # Si on clique dans la grille, on inverse l'état de la case
            if mouse_y < n_lignes * taille_case:
                i, j = mouse_y // taille_case, mouse_x // taille_case
                cellule[i, j] = not cellule[i, j]

            # Bouton pour activer/désactiver l'application des règles
            if bouton_rect.collidepoint(event.pos):
                z = True
            elif bouton_stop.collidepoint(event.pos):
                z = False
            elif bouton_quit.collidepoint(event.pos):
                pygame.quit()
            elif bouton_clear.collidepoint(event.pos):
                erase_cell()
            elif bouton_rdm.collidepoint(event.pos):
                cellule = np.random.choice([True, False], (n_lignes, n_colonnes))

                
                 
    if z:
        frame += 1
        appliquer_regles()

    # Dessiner chaque case de la grille (rouge pour actif, blanc pour inactif)
    tot_viv = 0
    for i in range(n_lignes):
        for j in range(n_colonnes):
            if cellule[i,j]:
                tot_viv += 1
                couleur = (100,100,100)
            else:
                couleur = (200,200,200)
            pygame.draw.rect(
                fenetre, couleur,
                pygame.Rect(j * taille_case, i * taille_case, taille_case, taille_case)
            )

    # Dessiner les boutons
    pygame.draw.rect(fenetre, (0, 200, 0), bouton_rect)
    font = pygame.font.Font(None, 24)
    texte = font.render("Lancer", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_rect.x + 10, bouton_rect.y + 5))

    pygame.draw.rect(fenetre, (232, 62, 51), bouton_stop)
    texte = font.render("Stop", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_stop.x + 10, bouton_stop.y + 5))

    pygame.draw.rect(fenetre, (223, 48, 130), bouton_quit)
    texte = font.render("Quit", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_quit.x + 10, bouton_quit.y + 5))
    
    pygame.draw.rect(fenetre, (222, 130, 5), bouton_frame)
    texte = font.render(f"Frame {frame}", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_frame.x + 10, bouton_frame.y + 5))
    
    pygame.draw.rect(fenetre, (77, 48, 223), bouton_cell)
    texte = font.render(f"Cellules {tot_viv}", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_cell.x + 10, bouton_cell.y + 5))
    
    pygame.draw.rect(fenetre, (48, 223, 220), bouton_clear)
    texte = font.render(f"Clear", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_clear.x + 10, bouton_clear.y + 5))
    
    pygame.draw.rect(fenetre, (113, 125, 126), bouton_rdm)
    texte = font.render(f"Random", True, (255, 255, 255))
    fenetre.blit(texte, (bouton_rdm.x + 10, bouton_rdm.y + 5))
    
    
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
