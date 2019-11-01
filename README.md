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
    
# v3.0 Release notes (24 oct.)
## Majeur
  - Modification du fichier mot.txt pour ajouter à chaque paire de mot sa difficulté
  - Modification de la procédure controle()
    - ``[cahier des charges] ``
    - A chaque faute, la difficulé du mot augmente de 6 
    - Il faut répondre juste 2 fois de suite uniquement lors du controle pour pouvoir annuler par soustraction les 6 points de difficultés. Mais si le joueur quitte avant d'avoir répondu 2x juste alors
      - Si les points de difficultés tendent plus vers la dizaine inférieur Arrondire les points de diff à la dizaine inférieur
      - Si les points de difficultés tendent plus vers la dizaine supérieur et que comme l'utilisateur a quitter son apprentissage, le temps qu'il revienne il aura plus de mal à se souvenir de ses mot difficiles donc arrondire les points de diff à la dizaine supérieur
    - ``[Algorithme]``
    - Incrémenter 6 à l'index du mot correspondant de la liste pointF
    - Lors de la fermeture de programme enregistrer chaque index de la liste pointF au mot correspondant :
      - Diviser par 10 la valeur 
      -  Arrondire à l'entier inférieur si la décimale est comprise entre [1, 3]
      - Arrondire à l'entier supérieur si la décimale est comprise entre [4, 9]
## Mineur
  - Amélioration de la procédure ``pendu()``:
    - Si l'utilisateur saisie 'exit' comme lettre :
      - Appeler ``vie`` restante fois la procédure ``life(vie)`` pour afficher la ``potence`` en entier
      - Affecter à vie ``0`` pour sortir du de la boucle while et afficher la réponse sans passer par les conditions additionnels (if... and r != "exit")
    - Ajout de la ``première`` lettre dès le départ, comme les règles officiel
  - Suppresion de la variable ``global N`` à cause du mini menu de la procédure hard()
    - Remplacement du N global par un ``N local`` dans chaque procédure
  - Optimisation de la demande de traduction dans les procédures test() et controle()
  - Ajout d'un Copy Right 
      
      
      
