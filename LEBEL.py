####################################################################
# Copyright (C) 2019-2019 BADER Alexandre <alexandrebader3@gmail.com>
#
# This file is part of LEBEL.
#
# LEBEL can not be copied and/or distributed without the express
# permission of Alexandre
####################################################################

# Ce programme est la v3.1 du projet LEBEL
# Debuté le 24/10/19 et fini le 28/10/2019
# Par Alexandre BADER

# Définie la procédure apprendre() avec les paramètres <list1>et  <list2>
def apprendre(list1, list2):
    # Cette procédure permet d'apprendre
    # tout les mots en les affichant un part un
    # Initialisation de <int> <N> au nombnre d'index que contient la liste <str> list1
    N = len(list1)
    print("Bienvenue dans le mode APPRENDRE\n")
    for i in range(N):      # Pour iallant de 0 à N
        # Affiche le mot de la list1 et sa traduction de list2
        print(i+1, '. ', list1[i], ' = ', list2[i], sep='', end=' ')
        input()  # attend que l'utilisateur ai retenue les 2 mots
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de l'apprentissage\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure reviser() avec les paramètres <list1>, <list2> et <list3>
def reviser(list1, list2, list3):
    # Cette procédure permet de réviser ses mots
    # avec un simple affichage du mot de la langue choisit
    # quand l'utilisateur à trouver la traduction dans sa tête
    # il peut vérifier si cette dernière est juste en affichant la traduction correcte
    N = len(list1)      # Initialisation de <int> <N> à la longeur de la list1
    print("Bienvenue dans le mode REVISER\n")
    # Demande si l'utilisateur veut afficher les mots à traduires en langue 1 ou langue 2 (de la list3)
    print("Vous voulez réviser en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()    # Saisir la langue voulu
    # list1 et list2 sont des adresses des listes misent en paramètres lors de l'appelle de cette procédure
    # Afin de ne pas modifier les listes de mot global dans le programme principal
    # Une copie des valeurs des 2 listes par adresse est effectuer
    # sur leurs intervalles complets [:] = [0:len(list)]
    # Copie des liste <list1> et <list2> dans <fr> et <et>
    fr, et = list1[:], list2[:]
    for i in range(N):      # Pour i allant de 0 à N
         # affecter à r une nombre aléatoires compris entre 0 et la longeur de <fr> -1 (pour ne pas dépasser l'index maximal de la liste)
        r = randint(0, len(fr)-1)
        if langue == '1':   # Si la langue désirer est la première de la list3
            # Affecter à mot le mot <str> d'index r de <fr>(list1) et à trad sa traduction qui est l'index r de <et>(list2)
            mot, trad = fr[r], et[r]
        else:               # Si la langue choisit est la deuxième
            # Affecter à mot le mot <str> d'index r de <et>(list2) et à trad sa traduction qui est l'index r de <fr>(list1)
            mot, trad = et[r], fr[r]
        print("La traduction de <", mot, "> est...", sep='',
              end='')        # Affiche le premier mot
        input()     # Attend que l'utilisateur trouve la traduction dans sa tête
        print('>', trad, end='')  # Affiche la bonne traduction
        input()     # Attend que l'utilisateur appuye sur entrée pour passer au mot suivant
        del fr[r]   # Supprime le mot fr d'index r pour ne pas qu'il soit réutiliser
        del et[r]   # Supprime le mot fr d'index r pour ne pas qu'il soit réutiliser
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de la revision\nAppuiez sur entrée pour revenir au menu...")

# Définie la fonction test() avec les paramètres <list1>, <list2> et <list3>
def test(list1, list2, list3):
    # Cette procédure permet de tester ses connaissaces
    # sans que la note n'est d'impacte sur le fichier score ou la variable pointFAible
    # Le test est semblable à reviser() à la différence que la traduction doit être écrite
    # Puis le script vérifie si cette réponse correspond à la tradcution
    # si, ce n'est pas le cas afficher directement la bonne réponse
    global base     # Informe au programme que la variable base peut être utiliser partout
    N = len(list1)      # Initialisation de <int> <N> à la longeur de la list1
    p = 0       # Initialisation de <int> <p> (pour point) à 0
    print("Bienvenue dans le mode TEST\n")
    # Demande si l'utilisateur veut afficher les mots à traduires en langue 1 ou langue 2 (de la list3)
    print("Vous voulez réviser en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()        # Saisir la langue voulu
    fr, et = list1[:], list2[:]     # Copie des liste <list1> et <list2> dans <fr> et <et>
    for i in range(N):      # Pour i allant de 0 à N
        # Affecte à r un entier aléatoire entre 0  et len(fr)-1
        r = randint(0, len(fr)-1)
        if langue == '1':   # Si la langue désirer est la première de la list3
            # Affecter à mot le mot <str> d'index r de <fr>(list1) et à trad sa traduction qui est l'index r de <et>(list2)
            mot, juste = fr[r], et[r]
        else:
            # Affecter à mot le mot <str> d'index r de <et>(list2) et à trad sa traduction qui est l'index r de <fr>(list1)
            mot, juste = et[r], fr[r]
        # Demande la tradcution de la variable <str> mot
        print("Donne moi la traduction de <", mot, '> : ', sep='', end='')
        reponse = input()       # Enregistre la réponse dans la variable <str> reponse
        if reponse == juste:    # Si la réponse est identique à la bonne traduction
            print(">BRAVO !")
            p += 1          # Incrémenter 1 à la variable p
        else:
            print(">FAUX, la réponse était <", juste, '>',
                  sep='')     # Affiche la bonne traduction
        # Supprime l'index r de la lsite <fr> pour ne pas que la fonction randint() ressorte le même index
        del fr[r]       # Supprime l'index <r> de la liste <fr>
        del et[r]       # Supprime l'index <r> de la liste <et>
    # Affiche la note sur le nombre total de mot et la note sur <base>
    print("\nFin du test ", p, "/", N,
          ' (', int(p/N*base), '/', base, ')', sep='')
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure controle() avec les paramètres <list1>, <list2> et <list3>
def controle(list1, list2, list3):
    # Cette procédure est la plus avancé dans l'apprentissage des mots
    # Chaque bonne et mauvaise réponses ont un impacte sur la liste pointF(list3)
    # La variable <note> est affecté à la variable score du controle si, ce dernier est meilleur que la varaible note
    global base, note   # Déclaration des variable <base> et <note> comme étant global donc utilisable partout
    N = len(list1)      # Initialisation de la variable <int> <N> à la longueur de <list1>
    print("Bienvenue dans le mode CONTROLE\n")
    fr, et = list1[:], list2[:]     # Copie des liste <list1> et <list2> dans <fr> et <et>
    p = 0  # Nomre de point pour chaque réponse juste
    corrige = []    # Initialisation à vide de la liste <str> <corrige>
    for i in range(N):  # Pour i allant de 0 à N
        r = randint(0, len(fr)-1)   # Choisit un rang <r> entre 0 et la longeur de <fr> -1
        if randint(0, 1):       # Une chance sur deux de traduire le mot dans la langue 1 ou 2
            mot, juste = fr[r], et[r]   # Affecte les mots du rang <r> des listes <fr> et <et> dans les variables string <mot> et <juste>
            corrige.append(mot)     # Ajoute à la liste corrige le mot à traduire <mot>
            index = list2.index(juste)  # Affecte à la variable <int> <index> l'index i du mot <juste> de la liste <list2>
                                        # Grâce la fonction .index() qui va retourner l'index de la valeur rechercher dans la liste demander
        else:   # Le mot à traduire sera en langue 2
            mot, juste = et[r], fr[r]   # Affecte les mots du rang <r> des listes <et> et <fr> dans les variables string <mot> et <juste>
            corrige.append(mot)     # Ajoute à la liste corrige le mot à traduire <mot>
            index = list1.index(juste)  # Affecte à la variable <int> <index> l'index i du mot <juste> de la liste <list2>
        # Affiche le mot à traduire <mot> en précisant combien il en reste en affichant sur <N> la variable local <i>
        print(i+1, '/', N, ' <', mot, sep='', end='> : ')
        reponse = input()   # Saisir la tradution dans la variable <str> <reponse>
        if reponse == juste:    # Si la réponse correspond bien à la bonne tradution
            # Script pour gérer les point faibles du mot actuelle
            if list3[index] > 0:    # Si le mot actuelle est une difficulté
                list3[index] -= 3   # Enlever 3 point de difficulté pour avoir eu juste
                if list3[index] < 0:    # Si la nouvelle valeur de l'index <index> de la liste <list3> est négative
                    list3[index] = 0    # Remettre la valeur à 0
            p += 1  # Ajoute 1 point à la variable <p> pour la note
            del corrige[-1] # Supprime le dernier élément de <corrige> car le mot demandé à  bien été traduit
        else:       # Sinon (si la traduction saisie est fausse)
            list3[index] += 6   # Ajouter à lindex de la liste des point faibles 6 points de difficulté
            corrige.append(juste)   # Ajoute le mot juste à la liste <corrige>
            if reponse:     # Si la traduction saisie contient au moins 1 caractère (!=vide)
                corrige.append(reponse)     # Ajouter à la lsite <corrige> la réponse fausse saisie <reponse>
            else:   # Sinon (si la réponse est vide)
                corrige.append('<vide>')    # Informe que la réponse était vide
        # Supprime l'index r de la lsite <fr> pour ne pas que la fonction randint() ressorte le même index
        del fr[r]   # Supprime l'index <r> de la liste <fr>
        del et[r]   # Supprime l'index <r> de la liste <et>
    score = round(p/N*base)     # Convertie la note sur la base définie
    print("\nFin du contrôle ", score, '/', base, sep='')   # Affiche le score sur la base (ex 10/20)
    if p != N:  # Si Il y a eu au moins 1 fautes
        reponse = input("Voulez voir le corrigé ? (Y/n) : ")    # Demande d'afficher le corriger
        if reponse == 'Y':  # Si l'utilisateur valide la demande
            for i in range(N-p):     # Pour i allant de 0 à N-p (= nombre de fautes)
                # Affiche Le mot suivit de sa tradution et la mauvaise tradution répondue
                # Pour afficher ces 3 éléments de la liste <corriger>
                # L'index i de la boucle for est multiplié part 3 puis il y est ajouter l'entier (1 ou 2) pour acccéder à l'élément voulu
                print(i+1, '/', N-p, " La traduction de ",corrige[i*3], " est <", corrige[i*3+1], "> (≠", corrige[i*3+2], ")", sep='', end='')
                input()     # Attendre que l'utilisateur prenne connaissance de son erreur
            print()     # Saute une ligne
    # La variable <note> est affectée à la variable <score> du contrôle
    # si cete dernière est meilleure que la varaible note
    if score > note:
        note = score # <note> étant une variable global sa nouvelle valeur sera conservée à la sortie de la procédure
    if p == N or reponse == 'Y':    # Si il n'y a pas de corrige ou à l'inverse si le corrige à bien été lu
        # Pour ne pas avoir un retour trop brusque sur le menu
        input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure hard() avec les paramètres <list1>, <list2>, <list3> et <list4>
def hard(list1, list2, list3, list4):
    # Cette procédure est la plus complexe du fait de la difficulté à gérer les difficultées des mots individuellement
    # Après une analyse et triage de tous les points de difficultés de la liste <list3>
    # Un sous menu est lancé semblable au menu principale 
    # à la différenc prêt que les mots mis en arguments correspondes uniquement au mot à point faibles
    # Ici les points de déifficultés ne peuvent être modifiés
    # Il faut se rendre dans le menu principale et lancer un controle() pour réduire ces pointF  
    N = len(list1)      # Initialistion de la variable <int> <N> au nombre de mot contenue dans <list1>
    print("Bienvenue dans le mode POINT FAIBLE\n")    # Affiche un petit message de bienvenue
    # initialisation du tableau <top> 
    # La première liste du tableau correspond à la copie de la list3 contenant les pointF de chaque mot
    # La deuxième liste du tableau contient une suite arithmétique de raison 1 
    # Cette suite sert à garder l'index correspondant au mot une fois le tableau trier par les pointF de la 1ere liste
    top = [list3[:], [i for i in range(len(list3))]]    # Initialisation du tableau <int> <top>
    # La 2eme liste est égale à i Or i correspond à la variable de la boucle pour i allant de 0 à longueur de <list3>
    # Donc la 2eme liste comprendra tout les entiers positifs de 0 à longueur de <list3>
    trier = True    # Initialisation de la variable <bool> <trier> à l'état True pour entrer dans la boucle while
    while trier:    # Tant que <trier> n'est pas égale à rien (!=0)
        trier = False   # Conjecturer que la liste 1 du tableau <top> est bien trier dans l'ordre décroissant des pointF
        for i in range(len(top[0])-1):      # Pour i allant de 0 au nombre de pointF -1
            if top[0][i] < top[0][i+1]:     # Si la valeur la plus grande dans l'intervalle [i;i+1] est à droite de la liste
                trier = True    # Affecter à <trier> l'état True pour continuer à trier
                for j in range(2):  # Répéter 2 fois
                    top[j][i], top[j][i+1] = top[j][i+1], top[j][i] # Inverser les valeurs i et i+1 de la 1ere et 2eme liste du tableau <top> 
    # Vérifie si la première liste de <top> contient que des 0
    if top[0].count(0) == len(top[0]):      # Si le nombre par la fonction .count() de 0 dans la liste d'index 0 de <top> est le même que la longueur de cetet même liste
        print("Félicitation ! Vous n'avez aucune difficultée :)")   # Cela signifie qu'il n'y a aucun mot qui pose difficulté
        input("\nAppuyez sur entrée pour revenir au menu...")
    else:
        print("Ce mode analyse vos points faibles\nEt vous permet de vous concentrez sur vos difficultées\n")
        if 0 in top[0]: # Si il y a au moins un 0 dans la 1ère liste 
            total = top[0].index(0) # Le nombre total de mot difficiles correspond au permier rang contenant un 0 (car la liste commence à l'index 0) 
        else:   # Si tout les mots ont des difficultées
            total = N   # <int> <total> est égale au nomre de mot <N>
        if total > 1:   # Si il y a plus d'un mot difficiles
            print("Tu as", total, "difficultées sur", N, "mots\n")  # Affiché la proportion de difficulté sur le nombre total <N> de mot
        n = total   # copie de <total> dans la variable <n> qui correspond au nombre de mot à travailler
        if n > int(N/2):    # Si la proportion des mot mot à difficultés est supérieur que tout les mot / 2
            n = 0   # Reset <n> à 0
            pc = int(input("Quelle quantitée en % voulez vous trvailler ? : ")) # Convertie la saisie en <int>
            n = int(pc * total / 100)   # Produit en croix pour obtenir la quantité n de mot à travailler en fonction du % du total des mots à travailler
            if n < 1:   # Si le produit en croix donne 0
                n = 1   # Forcer le nombre de mot à travailler à être supérieur à 0
        if n == 1:  # Si il n'y a qu'un seul mot à travailler
            print("Tu as une difficultée :")
        else:   # sinon; Si il y a plus d'un mot à traivailler
            print("Tes mots les plus difficiles sont dans l'ordre décroissant : ")
        # Afficher les mot difficiles avec leurs points de difficultés, précédament trié dans l'ordre décroissant 
        for i in range(n):  # Pour i allant de 0 à n 
            print('<', list1[top[1][i]],'>(', top[0][i]/10, ')', sep='', end='  ')  # Affciher l'index i de la 1ère et 2eme liste du tableau <top>
        # Ces 2 lignes suivantes sont très compressées et donc optimisées
        # Prenons l'exemple de <motFR>
        # La lsite est initialiser depuis la liste <list1> qui contient TOUT les mots en français
        # Or nous ne voulons que les mots à travailler donc difficiles
        # Pour se faire seul les mots de <list1> dont leurs index correspondent au valeurs de la 2eme liste du tableau <top> sont utilisés
        # Afin d'accéder à tout les index voulu, la boucle for est appellée
        # pour affecter chaque mot de <list1> d'index (valeur du 2eme tableau) i dans la liste <motFR>
        motFR = [list1[top[1][i]] for i in range(n)]    # Initialisation de <str> <motFR>
        motET = [list2[top[1][i]] for i in range(n)]    # Initialisation de <str> <motET>
        play = True     # Initialisation de la la variable <bool> à l'état True pour entrer dans la boucle while
        while play:     # Tant que play != 0
            # Afficher le sous menu de la procédure hard()
            # Son fonctionnement est le même que le menu principal
            print("\n\nQue veux tu faire pour t'améliorer ? ")
            print("1. Apprendre")
            print("2. Reviser")
            print("3. Test")
            print("4. Quitter(Menu)")
            choix = input("Lancer le mode :")
            print()
            if choix == '1':
                apprendre(motFR, motET) # Appel de la procédure apprendre() avec comme arguments <motFR> et <motET >
            elif choix == '2':          # Et non <list1> car on veut travailler que sur les mot à difficultés 
                reviser(motFR, motET, list4)    # Appel de la procédure reviser() avec comme arguments <motFR>, <motET> et <list4>
            elif choix == '3':
                test(motFR, motET, list4)   # Appel de la procédure test() avec comme arguments <motFR>, <motET> et <list4>
            elif choix == '4':
                play = False    # Sortir de la boucle while
            else:
                print("Choix inconnu, erreur...")

# Définie la procédure pendu() avec les paramètres <list1>, <list2> et <list3>
def pendu(list1, list2, list3):
    # Le jeu du pendu à été créer
    # pour se détendre entre deux séance de test() ou controle()
    # Il permet aussi de reviser l'écriture d'un mot
    # Le principe de jeux est simple
    # Après avoir choisi la langue du mot à trouver
    # Afficher le mot en cachant ses lettres part des '_' (sauf la première)
    # A chaque bonne lettre, remplacer '_' par la bonne lettre
    # A chaque mauvaise lettre, enlever un point de vie et afficher la potence
    def espace(mot):    # Définie la fonction espace() avec le paramètre <mot>
        # Retourne la chaine de caractère <mot> avec des espaces entre chaque caractères
        a = ''      # Initialise la variable a <str> à une chaine de caractère vide
        for i in mot:  # Pour i allant de 0 à longueur du paramètre
            a += i + ' '    # Ajouter par concaténation à a la lettre i du mot et un espace =' '
        return a    # retourner a 
    def check(lettre):      # Définie la fonction check() avec le paramètre <lettre>
        # Cette fonction vérifie si la lettre propsoer est dans la variable word
        # Si c'est le cas retourner False
        # Si la lettre proposer n'est pas dans la variable <str> word retourner True
        # Vérifie dans un premier temps si la lettre est valide pour être comparer avec <word>
        # Si la longueur est différente de 1 et différente de 'exit'
        if len(lettre) != 1 and lettre != 'exit':
            print('Erreur...')      # Afficher "Erreur"
            return 0        # Sortir de la fonction en retournant 0
        # Vérifie dans un second temps si la lettre n'a pas déjà été utilisée
        if lettre in use:   # Si la liste <use> contient la lettre
            print('Vous avez déjà utilisé cette lettre...')
            return 0    # Sortir de la fonction en retournant 0
        perdu = True    # Conjecture que la lettre n'est pas dans word
        # Si la lettre est valide, vérifier si elle appartient à <word>
        for i in range(len(find)):  # Pour i allant de 0 à la longueur de la lsite <find>
            # Si la lettre correspond à l'index i du mot à trouver <word>
            if lettre == word[i]:
                find[i] = lettre    # Affecter au rang i de <find> la lettre
                perdu = 0           # Sortir de la foncction en retournant False
                # Sinon si le mot <word> contient des accents (é, è,...)
                # et que la lettre est 'e'
                # alors si l'index i du mot à trouver <word> contient un des accents de la liste <checkE>
            elif accent == True and lettre == 'e' and (word[i] in checkE) == True:
                # Affecter au rang i de <find> la lettre d'index i du mot à trouver
                find[i] = word[i]
                perdu = 0   # Affecter à perdu False
        return perdu  # retourner la variable <bool> perdu

    def graph(vie, affiche):      # Définie la fonction graph() avec les paramètres <vie> et <affiche>
        # Cette profcédure affiche un dessin d'une potence dans le terminal avec des '#'
        # Définie la fonction l() pour ligne avec les paramètre <ligne>, <mini> et <max>
        def l(ligne, mini, max):
            # Cette procédure affecte l'intervale [mini;max] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < max:   # Répéter jusqu'à que la variable mini soit égale à max
                # Affecter au rang <mini> de l'index <ligne> du tableau <potence> le caractère '#'
                potence[ligne][mini] = '#'
                mini += 1       # Incrémente 1 à la variable <int> mini

        # Définie la fonction c() pour colonne avec les paramètre <colonne>, <mini> et <max>
        def c(colonne, mini, max):
            # Cette procédure affecte l'intervale [mini;max] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < max:   # Répéter jusqu'à que la variable mini soit égale à max
                # Affecter au rang <mini> de l'index <colonne> du tableau <potence> le caractère '#'
                potence[mini][colonne] = '#'
                mini += 1   # Incrémente 1 à la variable <mini>
        # En fonction des vies restantes ajouter les différentes parties (poutre(verticales, horizontales), corde,...) de la potence
        if vie == 7:
            # 1ère poutre horizontal
            l(7, 0, 9)  # Apelle de la fonction l() avec 7, 0, 9 en arguments
        elif vie == 6:
            # 2eme poutre appartenant et perpendiculaire à la première
            c(3, 2, 7)  # Apelle de la fonction c() avec 3, 2, 7 en arguments
        elif vie == 5:
            # 3eme poutre parallèle à la première, passant par le segment de la 2eme poutre et perpendiculaire à cette dernière
            l(1, 3, 13)  # Apelle de la fonction l() avec 1, 3, 13 en arguments
        elif vie == 4:
            # Bout de bois de maintien dans le coin de la 3eme et 2eme poutres
            # Affecter au rang 4 de l'index 3 du tableau <potence> le caractère '#'
            potence[3][4] = '#'
            # Affecter au rang 6 de l'index 2 du tableau <potence> le caractère '#'
            potence[2][6] = '#'
        elif vie == 3:
            # Corde
            # Affecter au rang 12 de l'index 12 du tableau <potence> le caractère '#'
            potence[2][12] = '|'
        elif vie == 2:
            # Tête
            # Affecter au rang 2 de l'index 3 du tableau <potence> le caractère '#'
            potence[3][12] = '0'
        elif vie == 1:
            # Tronc du corps
            c(12, 4, 7)  # Apelle de la fonction c() avec 12, 4, 7 en arguments
        elif vie == 0:
            # Bras du corps
            l(4, 10, 15)    # Apelle de la fonction l() avec 4, 10, 15 en arguments
        # Si le parmamètre affiche est vrai alros afficher la potence
        if affiche == True:
            # Double boucle pour afficher le tableau à 2 dimenssions
            for i in range(8):
                for j in range(17):
                    print(potence[i][j], end='')
                print()  # Revenir à la ligne après chaque affichage d'une ligne

    def gagner(vie):    # Définie la fonction gagner() avec le paramètre <vie>
        # Cette fonction permet de vérifier si toutes les lettres ont été trouvées
        # Si c'est le cas la fonction renvoie -1
        # pour sortir de la boucle et ne pas passer part la condition <if vie == 0>
        # Si il reste des lettres introuvées la fonction renvoie la même vie reçu en paramtère
        for i in find:  # Pour i allant de la lettre d'index 0 du mot find à sa dernière
            if i == '_':    # Si la lettre est égale à une letre pas encore trouvée
                return vie  # Renvoyer la vie actuelle
        return -1   # Si la boucle s'est fini (sans return) alors renvoyer -1

    # programme principal
    vie = 8     # Initialise la variable <int> <vie> à 8
    accent = False  # Conjecture que le mot n'a pas d'accent (é, è, ê,...)
    # Avec l'initialisation de la variable <bool> <accent>
    use = []        # Initialise la liste <str> <use> des mots utilisées
    potence = []    # Initialise le tableau (liste à 2 dimmensions) <str> <potence> pour afficher la potence
    print("Bienvenue dans le jeux du PENDU\nTapez 'exit' pour abandonner\n")
    # Demande dans quel langue le mot à trouver doit être
    # En fonction des index 0 et 1 de <list3>
    print("Vous voulez jouer en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()    # Enregistre la réponse dans la variable <str> langue
    if langue == '1':   # Si la langue choisit est la première de <lit3>
        # Affecter à word un mot aléatoire de tout les mots de la liste <list1>
        word = list1[randint(0, len(list1)-1)]
    else:   # Sinon
        # Affecter à word un mot aléatoire de la liste <list2>
        word = list2[randint(0, len(list2)-1)]
    # Initialiser la liste <checkE> correspondant aus accents de al lettre 'e'
    checkE = ['é', 'è', 'ê', 'ë']
    # Initialisation du mot à trouver <find> par une liste <str> contenant des caracrtères underscore
    find = ['_']*len(word)
    # fois la longueur du mot à trouver <word>
    # Analyse du mot <word> afin de trouver si :
    # 1.Il comporte des 'e' avec accent
    # 2.Il comporte des caractères spéciaux (comme un tiret ou une apostrophe)
    #      qui devront être directements visibles dans le mot caché <find>
    #      Car ce n'est pas un lettre à trouver !
    for i in range(len(word)):  # Pour i allant de 0 à la longueur de <word>
        if word[i] in checkE:   # Si la lettre i de <word> appartient à la liste <checkE>
            accent = True       # Affecter à accent l'état True
        elif word[i] == "'":    # sinon si le ieme caractère de <word> est égale à "'" alors
            # Remplacer la valeur i de <find> par le même caractère i de <word>
            find[i] = "'"
        elif word[i] == '-':    # Sinon si l'index i de <word> contient nu autre caractère spécial
            # Rempalcer la valeur i de <find> par ce même caractère.
            find[i] = '-'
    # Initialisation du tableau 17x8 <potence> pour afficher graphiquement la potence et le pendu
    for i in range(8):  # Pour i allant de 0 à 8
        # Ajouter à la liste <potence>, une liste vide de 17 espaces ' '
        potence.append([' ']*17)
    # Afficher la première lettre du mot <word> dans la liste <find>
    find[0] = word[0]

    # Boucle principale du jeu pendu()
    # Tant qu'il reste de la vie ou que le mot est trouvé (vie=-1)
    while vie > 0:
        # Affciher le mot à trouver <find> avec la fonction espace()
        print(espace(find))
        # Semande de saisie d'une lettre dans la variable <str> <lettre>
        lettre = input("Entrez une lettre : ")
        # Vérifie si la lettre est juste avec l'appelle de la fonction check()
        # L'appelle de cette fonction se fait avec l'argument <lettre>
        # La fonction retourne soit True pour "la lettre est juste"
        # La fonction retourne False pour "la lettre ne correspond pas au mot <word>"
        if check(lettre):   # Si la fonction retourne False
            vie -= 1        # Retirer une vie à la variable <vie>
            use.append(lettre)  # Ajoute la lettre saisie dans la liste <use>
        if lettre == 'exit':    # Si la variable <lettre> contient la demande 'exit'
            # Passer une part une sans aficher la potence les vies jusq'à 0
            # Tout en appelant la procédure graph()
            # Pour affciher par la suite la potence en entier
            for i in range(vie):    # Pour i allant de 0 à <vie>
                graph(vie, False)   # Appelle de la procédure graph() avec comme arguments <vie> et 0
                vie -= 1        # Enlever 1 vie à la variable <vie>
        graph(vie, True)    # Afficher la potence grâce à l'argument True de la procédure graph()
        vie = gagner(vie)   # Envoie en argument <vie> à la fonction gagner() qui revoie la nouvelle valeur de <vie>
    if vie == 0:    # Si <vie> est nulle alors le mot n'a pas été trouver part manque de vie
        print('\nPERDU\nLe mot était <', word, '>', sep='') # Afficher la bonne réponse
    else:   # Sinon si <vie> = -1 cela signifie que le mot à été trouvé
        print(espace(word))     # Affiche le mot <word> avec la fonction espace()
        print('\nFELICITATION !')   # Affiche la récompense de l'utilisateur
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin du jeu pendu\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure parametre() avec les paramètres <list1>, <list2>, <list3> et <list4>
def parametre(list1, list2, list3, list4):
    # Cette procédure permet 3 actions:
    # 1.Ajouter des mots, afin de na pas à avoir le faire depuis un éditeur texte en dehors du progrmame
    # 2.Reset les point faibles, si par exemple une autre personne veut apprendre les mots
    # 3.Changer la base de note, si une note sur 10 ne vous convient pas vous pouvez la changer sur n'importe quelle autre base dans l'intervale [1; 51[
    #   Pour ne pas a avoir à changer la base à chaque redémarrage du programme, cette valeur est sauvegarder dans un fichier settings.txt
    global base, note   # Définie les variables <base> et <note> comme global car elles sont modifiées
    print("Bienvenue dans le menu paramtère !")
    play = True     # Initialise la variable <bool> <play> à True pour entrer dans la boucle while
    while play:     # Tant que play != 0
        # Affiche le sous menu
        print("\nQue souhaitez vous faire ?\n")
        print("1. Ajouter des mots")
        print("2. Reset pointF")
        print("3. Changer base note")
        print("4. Quitter(menu)")
        # Saisir le choix 1, 2, 3 ou 4
        choix = input("Executer le paramètre : ")
        print()  # Saute une ligne
        # Les conditions ne sont pas suivis par l'appelle d'une procédure car, en particulier dans le choix 3, des variables sont modifiées
        # Or ces variables sont utilisés en dehors de la procédure. Lors d'une création d'une procédure il faut donc les déclarer comme global
        # Car dans une fonction (ou proc) toutes les variables sont en priorité déclarer comme local
        # En créant donc une procédure dans une procédure, la première ne prendra en compte les variables global de cette dernière.
        # Et la déclaration en global de ces varaibles dans une procédure à l'intérieur d'une procédure ne fonctionne pas
        # Ainsi la solution est de rester sur une seule préocédure, pour pouvoir utiliser <global>
        # Et pour des raison de lisibilité 
        if choix == '1':    # Si le choix est égale à '1'
            # Pour ajouter des mots, 3 listes doivent être affectées : <list1>, <list2> et <list3>
            # Il n'y pas plus à faire, et ces mots seront bien enregistrés dans le fichier mot.txt lors de la fermeture du programme
            print("Pour ajouter des mots suivez les instructions !")
            ajout = True    # Initialise la variable <bool> <ajout> à True pour entrer dans la boucle while
            while ajout:    # Tant que ajout != 0
                print("Entrez le mot", list4[0], ': ', end='')  # Demande le premier mot dans la langue de l'élément 0 de <list4>
                # Ajoute le mot saisie par input() dans la liste <list1> qui est un paramètre par adresse
                # Donc la liste mise en argument lors de l'appelle de la procédure sera bien affectée
                list1.append(input())   # Ajoute le mot saisie dans <list1>
                print("Entrez sa traduction en", list4[1], ': ', end='')    # Demande la traduction du mot dans la langue de l'élément 1 de <list4>
                list2.append(input())   # Ajoute la traduction saisie dans <list2>
                list3.append(0)     # Ajoute 0 point de difficulté pour la nouvelle paire de mot
                if input("Encore un autre ? (Y/n) : ") != 'Y':  # Si la réponse ne correspond pas au 'Y' de Yes,  quitter la boucle
                    ajout = False   # Affecter à <ajout> la valeur 0 pour quitter la boucle while
        elif choix == '2':      # Si le choix est 'Reset les pointF'
            # Ce reset est déconsillé d'être effectuer car il ne sera plus possible de connaître ses plus grosses difficultées
            # C'est pourquoi une demande de confirmation est demander pour continuer
            if input("Cette commande est irréverssible ! Poursuivre ? (Y/n) : ") == 'Y':    # Si l'avertissement est accepté 
                # Affecter à tout les index de <list3> la valeur 0
                for i in range(len(list3)): # Pour i allant de 0 au nombre de valeur de <list3>
                    list3[i] = 0    # Affecter à l'index i de <list> la valeur 0
                print("La commande s'est bien terminée !")  # Confirme le reset
        elif choix == '3':  # Si le choix est centré sur la modification de la base pour les notes ()
            # Ce paramètre change la base de la note pour les procédures test() et controle() ainsi que l'enregistrement du meilleur score
            # de la partie dans le fichier score.txt Or si la base change la note du meilleur score change aussi !
            # Il faut donc reconvertir avec les produits en croix la note pour qu'elle corresponde avec la nouvelle base (ex : 5/10 -> 10/20)
            print("La base actuelle est de <note/", base, ">", sep='')  # Affiche la base actuelle avec la variable global <base>
            newBase = 100   # Pour rentrer dans la boucle while
            while newBase > 51 or newBase <= 0:     # Tant que la nouvelle base ne corresponde pas aux critères de validités
                newBase = int(input("Entrez votre nouvelle base : "))   # Saisir la nouvelle base dans <str> <newBase>
                if newBase > 51:    # Si la base est trop grande
                    print("La base doit être inférieur à 50 !")
                elif newBase <= 0:   # Si la base est négative ou nulle
                    print("La base doit être supérieur à 0 !")
            note = round(note / base * newBase)     # Convertir la note en fonction de la nouvelle base
            base = newBase  # affecter à la variable global <base>, la variable local <newBase>
        elif choix == '4':  # Si le chox signifie 'Sortir du sous menu pour retourner au menu principal'
            play = False    # Affecter à <play> la valeur 0 pour quitter la boucle while
        else:   # Si aucune des condition ne correspondent au choix
            print("Choix inconnu, erreur...")   # Informer que le choix n'existe pas
        # Pour ne pas avoir un retour trop brusque sur le menu
        # Mais uniqement si l'utilisateur sort d'une procédure
        if choix in ['1', '2', '3']:  # Si la variable <str> <choix> appartient à la liste des choix correspondants à une procédure  
            input("\nAppuiez sur entrée pour revenir au menu...")   # Bloque le programme jusq'à une action de l'utilisateur

# Définie la procédure save() avec les paramètres <list1>, <list2>, <list3>, <list4>, <base> et <note>
def save(list1, list2, list3, list4, base, note):
    # Cette procédure est déstiné à sauvegarder toutes les valeurs de variables ou listes dans des fichiers textes
    def arrondie(float):
        # Cette fonction arrondie() sert à renvoyer un arrondie d'un float à une decimal uniquement
        # 1.Multiplie le paramètre <float> par 10
        # 2.Convertie le produit <float> en <int> 
        # 3.Convertie la variable <int> en <str>
        # 4.Récupère le dernier caractère de la variable <str> (il correspond donc à la decimale)
        # 5.Convertie ce caractère <str> en <int>
        dec = int(str(int(float*10))[-1])   # Récupère LA décimale du paramètre <flaot> dans un entier <int>
        if dec < 5:     # Si la décimale du paramètre est strictement inférieur à 5
            return int(float)   # L'arrondie correspond à son entier inférieur
        else:           # Si la décimale du paramètre est suérieur ou égale à 5
            return int(float)+1 # L'arrondie correspond à son entier supérieur
    # Premier enregistrement des listes dans le fichier mot.txt
    # Ouverture du fichier "mot.txt" en lecture  
    # avec l'encodage Universal Character Set Transformation Format - 8 bits
    f = open("mot.txt", 'r', encoding='Utf-8')  
    for l in f:     # Lecture de tout le fichier texte
        if l == '\n':   # Si la ligne <l> est égale à un saut de ligne (=vide)
            break   # Sortir de la boucle for 
    save = f.readlines()    # Sauvegarder tout le reste du fichier texte à partir du saut de ligne dans la liste <save>
    f.close()   # Fermer le fichier mt.txt
    f = open("mot.txt", 'w', encoding='Utf-8')  # Ouverture du fichier mot.txt en écriture (écrase le fichier éxistant) avec l'encodage 'Utf-8
    f.write('['+list4[0]+'='+list4[1]+']\n')    # Ecrire su la première ligne du fichier les 2 langues entre crochet [langue1=langue2]
    # Ecriture de toutes les paires de mots avec leurs point de difficultés 
    # ligne part ligne : mot=saTradution.(pointDeDifficultés)
    for i in range(len(list1)):    #Pour i allant de 0 au nombre de mot total dans <list1> 
        f.write(list1[i] + '=' + list2[i] + '.('+str(arrondie((list3[i]+1)/10)) + ')\n')    # Enregistrement en écriture des 3 listes
    f.write('\n')   # Ecriture d'un saut de ligne
    for index in save:  # Ajout de la sauvegarde non utiliser dans le programme
        f.write(index)  # Ecriture ligne part ligne
    f.close()   # Fermeture du fichier mot.txt
    f = open("settings.txt", 'w', encoding='Utf-8')     # Ouverture du fichier settings.txt en écriture avec l'encodage 'Utf-8'
    f.write("base pour note = "+str(base))      # Enregistre la variable <base> 
    f.close         # Fermeture du fichier settings.txt
    if note > 0:    # Si la milleure note de la séance est supérieur à 0
        from datetime import datetime   # Importation de la focntion datetime du module datetime
        f = open("score.txt", 'a', encoding='Utf-8')    # Ouverture du fichier score.txt en écriture (ajout) avec l'encodage 'Utf-8'
        now = datetime.now()    # now est une class contenant la date et l'heure actuelle de l'ordinateur
        # Enregistrement du meilleur score avec la date et heure de la fin du programme
        f.write("Le "+now.strftime('%d/%m/%y à %H:%M\n') + "La meilleure note était : "+str(note)+'/'+str(base)+'\n\n')
        f.close     # Fermeture du fichier score.txt

# Définie la fonction init() pour 'initialisation'
def init():
    # Cette fonction renvoie toutes les variables et listes du programme principale
    f = open("mot.txt", 'r', encoding='Utf-8')      # Ouverture en lecture du fichier mot.txt avec l'encodage 'Utf-8'
    list1 = []      # Initialisation de la liste <list1>
    list2 = []      # Initialisation de la liste <list2>
    list3 = []      # Initialisation de la liste <list3>
    list4 = ['']*2  # Initialisation de la liste <list4> à deux index vide
    tout = []       # Initialisation de la liste <tout>
    read = f.readline()    # Lecture de la première ligne du fichier
    list4[0], list4[1] = read[1:3], read[4:6]     # Affectation des deux index de <list4> à l'intervale [1;3[ et [4;6[ de <read>
    read = f.readline()     # Lecture de la ligne suivante
    # Affecte à la liste <tout> tout les mots, leurs traductions et leurs point de difficultée appartenant 
    while read != '\n':     # Tant que la ligne lu n'est pas égale à '\n'
        tout.append(read)   # Ajouter à la liste <tout> le contenu de la ligne lu
        read = f.readline() # Lire la ligne suivante
    for mot in tout:    # Analyse de la liste <tout> index part index
        temp = ''   # Initialise <temp> pour temporaire à une chaine de caractère vide
        c = 0       # Initialise la variable <int> <c> à 0
        while mot[c] != '=':    # Tant que l'index c de la ligne <mot> de <tout> n'est pas égale à '='
            temp += mot[c]      # Affecter par concaténation à <temp> le caractère c de <mot>
            c += 1              # Incrémenter 1 à la variable <c>
        list1.append(temp)      # Ajouter à la liste <list1> le mot dans la langue1
        temp = ''       # Initialise <temp> à une chaine de caractère vide
        c += 1          # Incrémenter 1 à la variable <c> pour passer le caractère '='
        while mot[c] != '.':    # Tant que l'index c de la ligne <mot> de <tout> n'est pas égale à '.'
            temp += mot[c]      # Affecter par concaténation à <temp> le caractère c de <mot>
            c += 1              # Incrémenter 1 à la variable <c>
        list2.append(temp)      # Ajouter à la liste <list2> la traduction dans la langue2
        temp = ''       # Initialise <temp> à une chaine de caractère vide
        c += 1          # Incrémenter 1 à la variable <c> pour passer le caractère '.'
        while mot[c] != '\n':   # Tant que l'index c de la ligne <mot> de <tout> n'est pas égale à '\n'
            temp += mot[c]      # Affecter par concaténation à <temp> le caractère c de <mot>
            c += 1              # Incrémenter 1 à la variable <c>
        list3.append(temp)      # Ajouter à la liste <list3> les point de difficultés du mot <mot>
    # Enlève les parenthèses de chaque index i de <list3> et multiplie chque valeur par 10 après les avoir converties en <int>
    list3 = [int(i[1:len(i)-1])*10 for i in list3]      
    f.close()       # Ferme proprement le fichier mot.txt
    f = open("settings.txt", 'r', encoding='Utf-8')     # Ouverture en mode lectue avec l'encodage 'Utf-8' du fichier settings.txt
    base = ''   # Initialise la variable <str> <base> à rien
    read = f.readline()     # Lecture de la première ligne du fichier
    # Si le 2eme caractère en partant de la fin est un espace 
    # CEla signifie que la base est un chiffre d'une unnité
    if read[-2] == ' ':
        base = int(read[-1])    # Affecte à base le dernier élément de <read> convertie en <int>
    # Sinon, Si le 2eme caractère en partant de la fin n'est pas un espace 
    # Cela signifie que la base est un nombre d'une dizaine
    # Et pas plus car lors de son changement dans la procédure parametre() il est impossible de dépasser 
    else:
        base = int(read[-2:])  # Affecte à base les 2 derniers éléments de <read> convertie en <int>
    f.close     # Ferme le fichier settings.txt
    return list1, list2, list3, list4, base, 0      # Renvoie toutes les listes, variables et valeur demandé par l'appelle de la fonction init()

# PROGRAMME PRINCIPALE
from random import randint      # Importation de la fontion randint() du module random
# Affiche un messsage de bienvenue
print("Bienvenue dans <LE Boss En Langue> !")
# Initialise toutes les listes et variables avec la fonction init()
motFR, motET, pointF, langue, base, note = init()
play = True  # Initialisation de la variable <bool> play à True pour pouvoir rentrer dans la boucle while
# Tant que play n'est pas pas vide
# On peut aussi écrire <play != 0>
# Mais cette condition est moins performante car elle oblige l'ordinateur à effectuer 2 opérations
# (comparer play à une autre donnée : 0, puis évaluer si le résultat est True ou False)
while play:
    # Affichage du menu principale
    print("\n####### MENU ########")
    print("## 1. Apprendre    ##")
    print("## 2. Reviser      ##")
    print("## 3. Test         ##")
    print("## 4. Contrôle     ##")
    print("## 5. Point faible ##")
    print("## 6. Pendu        ##")
    print("## 7. Paramètre    ##")
    print("## 8. Quitter      ##")
    print("#####################")
    # saisir le choix dans la variable <str> choix
    choix = input("Lancer le mode : ")
    print()         # saute une ligne
    # compare le choix à 8 conditions différente en <str> (pour empêcher une erreur si un caractère est entré)
    if choix == '1':
        # Appel de la procédure apprendre() avec comme arguments motFR et motET
        apprendre(motFR, motET)
    elif choix == '2':
        # Appel de la procédure reviser() avec comme arguments motFR, motET et langue
        reviser(motFR, motET, langue)
    elif choix == '3':
        # Appel de la procédure test() avec comme arguments motFR, motET et langue
        test(motFR, motET, langue)
    elif choix == '4':
        # Appel de la procédure controle() avec comme arguments motFR, motET et pointF
        controle(motFR, motET, pointF)
    elif choix == '5':
        # Appel de la procédure hard() avec comme arguments motFR, motET, pointF et langue
        hard(motFR, motET, pointF, langue)
    elif choix == '6':
        # Appel de la procédure pendu() avec comme arguments motFR, motET et langue
        pendu(motFR, motET, langue)
    elif choix == '7':
        # Appel de la procédure parametre() avec comme arguments motFR, motET, pointF et langue
        parametre(motFR, motET, pointF, langue)
    elif choix == '8':
        play = False                # Affecte à play l'état False pour sortir de la boucle
    else:           # Si aucune des conditions ci dessus n'a été respectées alors
        # Informe que le choix saisie est invalide
        print("Choix inconnu, erreur...")
# Afficher "A bientôt" afin d'inciter le joueur à revenir
print("A bientôt !")
# appel de la fonction save() avec comme arguments toutes les variables et listes
save(motFR, motET, pointF, langue, base, note)
