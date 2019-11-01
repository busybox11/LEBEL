# LEBEL
### ``LEBEL`` (pour ``LE Boss En Langue`` jugez pas x) est mon premier mini projet pour l'ISN 

# Fonctionnement
Le but du programme est simple ! ``apprendre des mots dans une autre langue``

Pour se faire, 5 modes sont disponibles : 
### Apprendre
  1. Affichage ligne par ligne dans l'ordre les mots suivis de leurs traductions.
  2. Une fois le mot ``mémorisé``, appuyez sur la touche entrée pour passer au suivant
### Reviser
  1. Demander si les mots affichés doivent être en langue 1 ou langue 2.
  2. Affichage d'un mot ``aléatoire`` dans la langue sélectionnée. 
  3. Attendre jusqu'à l'appuie de la touche entrée pour afficher la ``réponse`` de la traduction 
### Test
  1. Demander si les mots affichés doivent être en langue 1 ou langue 2.
  2. Demande la ``traduction`` d'un mot aléatoire dans la langue sélectionnée.
  3. Pour chaque mauvaise réponse donner la bonne réponse.
  4. Affiche un ``score`` et une note sur 20
### Contrôle
  1. Demander si les mots affichés doivent être en langue 1 ou langue 2. 
  2. Demande ``aléatoirement`` la traduction de tous les mots, sans afficher la réponse
  3. Affiche un ``score`` et une note sur 20
  4. Demande l'afficahge des ``fautes`` (si présentes) ainsi que la ``correction``
  5. Si oui (Y) afficher ligne par ligne
     - Le mot du controle
     - Sa traduction corrigé
     - La traduction fausse de l'utilisateur
### Point faible
  1. Analyse et trie dans l'ordre ``décroissant`` les mots compliqués
  2. Demander quelle quantité de mot en pourcentage % travailler
  3. Affiche les mots affecté à des points de difficultés
  4. Lance un menu avec 3 modes : 
     - apprendre
     - reviser
     - test 
    
# v3.3 Release notes (31 oct.)
## Majeur
  - Ajout d'un menu graphique
    - Grâce au module ``turtle`` afficher un graphique sur un repère ``x, y``
    - Les ordonnées représentent la note sur 20 en fonction du temps (absisses) qui précisons, n'est pas à l'échelle
    - On peut afficher 2 catégories de note différentes :
      - Les dernières notes actuelles de la liste ``note`` C'est à dire les notes produites par ``controle()`` depuis l'ouverture du programme
      - Tous les meilleures notes du fichier ``score.txt``
    -  Avant de débuté le graphique il faut avoir convertie les notes sur une base de 20
## Mineur
  - Optimisation du script dans ``save()``
  - Il était inutile de récupérer à chaque note du fichier score.txt la base de la note, car elle est identique partout
    - La variable ``baseSave`` est donc affectée dès le début grâce à la deuxième ligne du fichier encadré ``#``
  - Changement de de la ``variable note`` en ``liste note`` pour le mode graphique 
    - La note enregistrée dans [score.txt](./score.txt) sera donc ``bestNote`` qui est la meilleure note de la liste <note>
  - Changement de barème sur les points de difficultés, ``3-->4`` donc si la réponse est juste dans ``controle()`` 
    - Retirer à l'index du mot de la liste ``pointF`` 4 points au lieu de 3 pour plus de diverssité dans les points faibles, plus de facilité pour le joueur 
  - Ajoute le ``Y`` minuscule lors des demandes de confirmations
