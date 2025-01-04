# 1. Presentation Générale 

## Titre : Fort Boyard

Contributeurs : Sélène AKDOGAN et Océanne TSANE


Description : Le Fort Boyard Simulator est un jeu où vous et votre équipe allez relever des défis dans 4 catégories (mathématiques, logique, hasard et énigmes). Vous devrez gagner 3 clés en réussissant les épreuves et, une fois ces clés obtenues, vous accéderez à l’épreuve finale. Si vous réussissez, vous débloquerez la salle du trésor et remporterez la victoire ! Un bonus permet de suivre les performances des joueurs et d'enregistrer les résultats dans un fichier.









Fonctionnalités principales : 
- Création et gestion de l'équipe
- Sélection et gestion des épreuves 
- Gagner des clés 
- Épreuve finale 
- istorique des performances (Bonus)
- Interaction utilisateur
- Choix aléatoire des épreuves



Technologies Utilisées : 
- Python
- Pycharm
- GitHub

Installation : Le projet se fait en binôme. Nous utiliserons Git et GitHub pour partager le code et travailler ensemble de façon fluide. Un membre crée le dépôt principal sur GitHub, l'autre le clone. Ensuite, chacun doit être ajouté comme collaborateur. 

Utilisation : Pour que tout le monde travaille sur la même version du code, il faut régulièrement récupérer les dernières modifications ("pull") et envoyer les siennes ("commit and push"). L’objectif est de garantir une bonne collaboration tout au long du projet.





# 2. Documentation Technique

Algorithme du jeu : 
Voici les différentes étapes de otre projet :
1. Epreuve mathématiques 
2. Epreuve Hasard
3. Epreuve Logique
4. Énigmes du Père Fouras
5. Épreuve finale (salle du trésor)
6. Finalisation des fonctions dans fonctions_utiles.py
7. Finalisation du fichier main.py


Details des fonctions implémentées :

### A. Fonctions Epreuve Mathématique :

- factorielle(n) :
Calcule la factorielle de n, Paramètre : n (int),
Retour : La factorielle de n.


- epreuve_math_factorielle() :Gère l’épreuve de la factorielle, génère un nombre aléatoire et vérifie la réponse du joueur, Paramètre : Aucun, Retour : True si la réponse est correcte, False sinon.


- resoudre_equation_lineaire() : Génère deux nombres aléatoires et résout l’équation linéaire ax + b = 0, Paramètre : Aucun, Retour : Un tuple (a, b, x) avec les valeurs aléatoires et la solution de l’équation.


- epreuve_math_equation() : Demande de résoudre une équation linéaire aléatoire et vérifie la réponse du joueur.
Paramètre : Aucun
Retour : True si la réponse est correcte, False sinon.


- epreuve_roulette_mathematique() : Génère cinq nombres aléatoires et effectue une opération (addition, soustraction ou multiplication) que le joueur doit résoudre.
Paramètre : Aucun
Retour : Le résultat de l’opération.


- epreuve_math_type() : Appelle une épreuve mathématique (roulette) et vérifie la réponse du joueur.
Paramètre : Aucun
Retour : True si la réponse est correcte, False sinon.


- epreuve_math() :  Sélectionne aléatoirement une épreuve mathématique et vérifie la réponse du joueur.
Paramètre : Aucun
Retour : Résultat de l’épreuve (True ou False)



### B.Fonctions Epreuve Hasard :
- bonneteau() : Implémente l’épreuve du bonneteau où le joueur doit deviner sous quel bonneteau se cache la clé parmi trois, avec deux tentatives.
Paramètre : Aucun
Retour : True si la réponse est correcte, False sinon.


- jeu_lance_des() : Gère le jeu de dés où le joueur et le maître du jeu lancent chacun deux dés et celui qui obtient un 6 en premier remporte la partie.
Paramètre : Aucun
Retour : True si le joueur gagne, False sinon.


- epreuve_hasard() : Sélectionne aléatoirement une épreuve de hasard (bonneteau ou lancer de dés) et retourne le résultat du jeu.
Paramètre : Aucun
Retour : Résultat de l’épreuve (True ou False)

### C. Fonctions Epreuve Logique : 
- afficher_grille(grille) : Affiche la grille du jeu Tic-Tac-Toe à chaque tour.
Paramètre : grille (liste 2D représentant l'état du jeu)
Retour : Aucun, juste l'affichage de la grille.


- verifier_victoire(grille, symbole) : Vérifie si un joueur (symbole "X" ou "O") a gagné en alignant ses symboles.
Paramètres :
grille (liste 2D représentant l'état du jeu)
symbole (caractère représentant le joueur, "X" ou "O")
Retour : True si le joueur a gagné, sinon False.


- grille_complete(grille) : Vérifie si la grille est complète, c'est-à-dire qu'aucune case n'est vide.
Paramètre : grille (liste 2D représentant l'état du jeu)
Retour : True si la grille est complète, sinon False.


- verifier_resultat(grille) : Vérifie le résultat du jeu (victoire ou match nul).
Paramètre : grille (liste 2D représentant l'état du jeu)
Retour : True si le jeu est terminé (victoire ou match nul), sinon False.


- coup_maitre(grille, symbole) : Détermine le coup du maître du jeu ("O") pour gagner, bloquer, ou jouer aléatoirement.
Paramètres :
grille (liste 2D représentant l'état du jeu)
symbole (caractère représentant le maître du jeu, "O")
Retour : Un tuple (i, j) représentant les indices de la case où le maître doit jouer.


- est_entier(valeur) : Vérifie si une valeur donnée peut être convertie en entier.
Paramètre : valeur (chaîne de caractères à vérifier)
Retour : True si la valeur peut être convertie en entier, sinon False.


- tour_joueur(grille) : Gère le tour du joueur (symbole "X") où il entre ses coordonnées pour jouer un coup.
Paramètre : grille (liste 2D représentant l'état du jeu)
Retour : Aucun, le coup est directement effectué sur la grille.


- tour_maitre(grille) : Gère le tour du maître du jeu (symbole "O") qui choisit une case pour jouer.
Paramètre : grille (liste 2D représentant l'état du jeu)
Retour : Aucun, le coup est directement effectué sur la grille.


- jeu_tictactoe() : Orchestration complète du jeu Tic-Tac-Toe entre un joueur ("X") et le maître ("O").
Paramètre : Aucun
Retour : True si le joueur "X" gagne ou s'il y a un match nul, False si le maître "O" gagne ou en cas de match nul.


### D. Fonctions Enigme Pere Fouras :
- charger_enigmes(fichier) :
Cette fonction lit un fichier JSON qui contient une liste d'énigmes.
Elle ouvre le fichier et charge son contenu dans une variable enigmes.
Elle retourne cette liste pour qu'elle puisse être utilisée plus tard.
Paramètres : fichier : Le chemin du fichier JSON contenant les énigmes.
Retour : Une liste d'énigmes, chaque énigme étant un dictionnaire avec une question et une réponse.



- enigme_pere_fouras(fichier) :
Cette fonction est responsable de la logique du jeu avec le Père Fouras. Elle pose une énigme aléatoire au joueur et vérifie ses réponses.
Elle commence par charger les énigmes via charger_enigmes().
Ensuite, elle choisit une énigme au hasard et l'affiche à l'utilisateur.
Le joueur a trois tentatives pour répondre correctement à l'énigme.
Si la réponse est correcte, le joueur gagne la clé. Sinon, il perd après trois tentatives.
Paramètres : fichier : Le chemin du fichier JSON contenant les énigmes.
Retour : True si le joueur trouve la bonne réponse.
False si le joueur échoue après trois tentatives, affichant la solution de l'énigme.

### E. Fonctions Epreuve Finale : 
- salle_De_Tresor(fichier)
Rôle : Jeu où le joueur doit deviner un mot-code en trois essais.
Paramètre : fichier (str) : Chemin du fichier JSON.


### F. Fonctions MAIN :
- jeu()
Rôle : C'est la fonction principale qui orchestre le déroulement du jeu. Elle gère l'introduction, la composition de l'équipe, le menu des épreuves, et la gestion des clés gagnées avant de lancer l'épreuve finale.
Paramètre : Aucun.
Retour : Aucun, mais affiche le résultat du jeu (victoire ou défaite) à la fin.





### Gestion des Entrées et Erreurs :

Comment les erreurs sont gérées :

- Si le joueur entre un numéro qui n'existe pas, il reçoit un message disant de réessayer.
- Si la réponse à une énigme est fausse, le joueur perd un essai et peut recevoir un nouvel indice.
- Problèmes avec les fichiers : Si les fichiers de données (JSON) sont manquants ou mal formatés, des erreurs peuvent apparaître. Ce serait mieux de gérer ça avec des messages d’erreur spécifiques.
Quelques bugs à connaître 

Les bugs connus :
- Le même message peut parfois être répété plus d'une fois.
- Problèmes avec les fichiers JSON : Si le fichier est  manquant, ça pourrait poser problème.
- Les indices supplémentaires ne sont pas bien gérés : Si tous les indices sont donnés, rien ne se passe.






# 3. Journal de Bord


### Chronologie du Projet :
- 20 Décembre 2024 : Finis l'épreuve Mathématique. Problème : Océanne n'avais pas d'ordinateur, donc on l'a fait sur l'ordinateur de Sélène ensemble (on l'avais commencé en classe)
- 22 Décembre 2024 : Finis l'épreuve Hasard. Aucun problème rencontré. (on l'avait aussi commencé en classe)
- 2 Janvier 2025 : Finis l'épreuve Logique et père fouras. Problème : l'ordinateur de Océanne bug, et son github ne fonctionne pas. Donc elle a envoyé  à Sélène le programme epreuve logique en photo, et sélène l'a copié sur son ordinateur. Mais le problème c'est que les pull ne seront pas affichés sur github. 
- 3 janvier 2025 : Finis l'épreuve fonctions utiles et main. Problème : c'etait compliqué.


Répartition des Tâches :
- Epreuve mathématiques : Océanne
- Epreuve Hasard : Sélène
- Epreuve Logique : Océanne (et Sélène)
- Epreuve pere fouras : Sélène
- Fonctions utiles : Sélène (avec Océanne)
- Main : Sélène (avec Océanne)






# 4. Test de Validation 


### Stratégies de Test :

Pour Epreuve mathématiques :
- test : Épreuve de Mathématiques: Calculer la factorielle de 3.
Votre réponse: 6
Correct ! Vous gagnez une clé.
Bravo, épreuve réussie ! Une clé a été gagnée.

  

Pour Epreuve hasard :
- test : Appuyez sur 'Entrée' pour lancer les dés du joueur
Le joueur a obtenu : 3 et 4
Appuyez sur 'Entrée' pour lancer les dés du maître du jeu
Le maître du jeu a obtenu : 5 et 4
Aucun joueur n'a obtenu un 6. Passons au prochain essai.
Il reste 2 essais
Appuyez sur 'Entrée' pour lancer les dés du joueur
Le joueur a obtenu : 1 et 6
Félicitations ! Le joueur a obtenu un 6 et remporte la partie et la clé.
Bravo, épreuve réussie ! Une clé a été gagnée.


Pour Epreuve logique : 
- test :   |   |  
---------
  |   |  
---------
  |   |  
---------
Entrez les coordonnées (ligne, colonne) pour votre coup (entre 1 et 3) : 1 1
X |   |  
---------
  |   |  
---------
  |   |  
---------
Coup du maître (O) :
X | O |  
---------
  |   |  
---------
  |   |  
---------
Entrez les coordonnées (ligne, colonne) pour votre coup (entre 1 et 3) : 1 3
X | O | X
---------
  |   |  
---------
  |   |  
---------
Coup du maître (O) :
X | O | X
---------
O |   |  
---------
  |   |  
---------
Entrez les coordonnées (ligne, colonne) pour votre coup (entre 1 et 3) : 3 3
X | O | X
---------
O |   |  
---------
  |   | X
---------
Coup du maître (O) :
X | O | X
---------
O | O |  
---------
  |   | X
---------
Entrez les coordonnées (ligne, colonne) pour votre coup (entre 1 et 3) : 3 2
X | O | X
---------
O | O |  
---------
  | X | X
---------
Coup du maître (O) :
X | O | X
---------
O | O | O
---------
  | X | X
---------
Le maître du jeu 'O' a gagné !
Dommage, épreuve échouée. Pas de clé cette fois.


Pour Epreuve Pere Fouras
- test : Énigme : Chaque année, il change sans cesse,
Qu'il soit critique ou bien ingrat,
De la fleur à la sagesse,
Son mystère demeure bien là.
Qui est-il ?
Votre réponse : ciel
Incorrect ! Il vous reste 2 essais.
Votre réponse : terre
Incorrect ! Il vous reste 1 essais.
Votre réponse : la terre
Vous avez échoué ! La solution était : L'Âge
Dommage, épreuve échouée. Pas de clé cette fois.



