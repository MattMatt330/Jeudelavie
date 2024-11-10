      Jeu de la vie
Version 1.0 du 10/11/2024

python 1.13.0

Bibliotèque nessesaires:
pygame [https://www.pygame.org/]
numpy [https://numpy.org/]


Ceci est un exercice que je me suis donné pour apprendre le code 
C'est une création francaise, donc le code sera en francais,
si tu ne le parle pas, apprend la langue de moliere !!!

Le jeu de la Vie est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. Il s’agit d’un automate cellulaire, un modèle où chaque état conduit mécaniquement à l’état suivant à partir de règles préétablies.

Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie mais pas là, dont les cases — appelées « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante '1' » ou « morte '0' ».

Une cellule possède huit voisines, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes :

        ----si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante.
        C’est le cas de la cellule verte dans la configuration de gauche ;

        ----si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à     l’étape suivante.
        Dans le cas de la configuration de gauche, la cellule située entre les deux cellules vivantes reste morte à l’étape suivante ;

        ----si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante.
        C’est le cas de la cellule rouge dans la configuration de gauche.

Histoire:

Le jeu de la Vie est inventé en 1970 par John Horton Conway, professeur de mathématiques à l’université de Cambridge, au Royaume-Uni.

J. H. Conway s’intéresse alors à un problème proposé par le mathématicien John Leech dans le domaine de la théorie des groupes et qui avait trait à l’empilement dense de sphères à 24 dimensions (connu comme le réseau de Leech). Il découvre quelques propriétés remarquables et publie les résultats de son étude en 1968. Conway est également intéressé par un problème présenté vers les années 1940 par un mathématicien renommé : John von Neumann.

Ce dernier a essayé de trouver une hypothétique machine qui pourrait s’autoreproduire. Il y parvient en construisant un modèle mathématique aux règles complexes sur un repère cartésien. Conway simplifie les idées de von Neumann en couplant ses résultats précédents sur les réseaux de Leech avec ses travaux sur les machines auto réplicantes, il donne naissance au "jeu de la Vie".

Le premier contact entre le grand public et ces travaux se fait en 1970 à travers une publication dans Scientific American dans la rubrique de Martin Gardner : « Mathematical Games »1.

Gardner écrit dans ses colonnes que « le jeu de la Vie » rendit Conway rapidement célèbre et il ouvrit aussi un nouveau champ de recherche mathématique, celui des automates cellulaires. En effet, les analogies du jeu de la Vie avec le développement, le déclin et les altérations d’une colonie de micro-organismes, le rapprochent des jeux de simulation qui miment les processus de la vie réelle. »

D’après Gardner, Conway expérimenta plusieurs jeux de règles concernant la naissance, la mort et la survie d’une cellule avant d’en choisir un où la population des cellules n’explose pas (ce qui arrive souvent lorsque les conditions de naissances sont moins strictes) mais où des structures intéressantes apparaissent cependant facilement. À l’origine, John Conway y jouait à la main, en utilisant un plateau de go pour grille et des pierres de go pour matérialiser les cellules vivantes.

Plusieurs structures intéressantes furent découvertes, comme le « planeur », un motif qui se décale en diagonale toutes les quatre générations, ou divers « canons » qui génèrent un flux sans fin de planeurs. Ces possibilités augmentent l’intérêt pour le jeu de la Vie. Sa popularité augmente d’autant plus vite à une époque où une nouvelle génération de mini-ordinateurs plus économiques est commercialisée, ce qui permet de tester des structures pendant la nuit, lorsque personne d’autre n'utilise les ordinateurs.

Vers la fin des années 1980, la puissance des ordinateurs est suffisante pour permettre la création de programmes de recherche de structures automatiques efficaces ; couplés au développement massif d’Internet, ils conduisent à un renouveau dans la production de structures intéressantes.

Au bout du compte, le jeu de la Vie attire plus l’intérêt du grand public sur les automates cellulaires (entre autres grâce à divers économiseurs d’écran) que, par exemple, tous les travaux de Edgar Frank Codd, spécialiste reconnu du domaine et auteur de l’ouvrage de référence Cellular automata (1968)