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
    
# v3.3.1 Release notes (31 oct.)
## Majeur
  - Ajout de de valeur (pas à l'échelle) sur l'axe des abscisses TEMPS du graphique
     - Si le graphique du fichier score.txt est tracé alors l'axe x sera composé des dates des meilleurs note
     - Si le graphique de la séance actuelle est tracé alors l'axe x sera composé des heures aux quelles controle() a été appelé
     - Pour rester lisible et par l'impossiblité d'affiché les valeurs sans qu'elles sont parallèles à l'axe 
     - Si le nombre de valeur est supérieur à 15, alterner la distance par rapport à l'axe x des valeurs lorsques elles sont imprimées
     - Si le nombre de valeur est supérieur à 30, supprimer les premières valeurs pour atteindre 30 au maximum
## Mineur
  - La liste ``note`` passe à tableau pour pouvoir enregistrer l'heure d'obtention de chaque note par la procédure ``controle()``
  - Comme chaque note à une heure, lors de la procédure ``save()`` enregistrer la date actuelle ainsi que l'heure de la note et non actuelle
