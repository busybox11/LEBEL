 ####################################################################
 # Copyright (C) 2019-2019 BADER Alexandre <alexandrebader3@gmail.com>
 #
 # This file is part of LEBEL.
 #
 # LEBEL can not be copied and/or distributed without the express
 # permission of Alexandre
 ####################################################################

 # Ce programme est la v3.0 du projet LEBEL
 # Debuté le 21/10/19 et fini le 24/10/2019 
 # Par Alexandre BADER

def apprendre(list1, list2):
    N = len(list1)
    print("Bienvenue dans le mode APPRENDRE\n")
    for i in range(N):
        print(i+1,'. ', list1[i],' = ', list2[i],sep='',end=' ')
        input()
    input("\nFin de l'apprentissage\nAppuiez sur entrée pour revenir au menu...")

def reviser(list1, list2, list3):
    N = len(list1)
    print("Bienvenue dans le mode REVISER\n")
    print("Vous voulez réviser en ",list3[0],'(1)/',list3[1],"(2) : ",sep='',end='')
    langue = input()
    fr,et = list1[:], list2[:]
    for i in range(N):
        r = randint(0, len(fr)-1)
        if langue == '1':
            print("La traduction de <",fr[r],"> est...",sep='',end='')
            input()
            print('>',et[r],end='')
        else:
            print("La traduction de <",et[r],"> est...",sep='',end='')
            input()
            print('>',fr[r],end='')
        input()
        del fr[r]
        del et[r]
    input("\nFin de la revision\nAppuiez sur entrée pour revenir au menu...")

def test(list1, list2, list3):
    N = len(list1)
    p = 0
    print("Bienvenue dans le mode TEST\n")
    print("Vous voulez réviser en ",list3[0],'(1)/',list3[1],"(2) : ",sep='',end='')
    langue = input()
    fr,et = list1[:], list2[:]
    for i in range(N):
        r = randint(0, len(fr)-1)
        
        if langue == '1':
            mot = fr[r]
            juste = et[r]
        else:
            mot = et[r]
            juste = fr[r]
        print("Donne moi la traduction de <",mot,'> : ',sep='',end='')
        reponse = input()
        if reponse == juste:
            print(">BRAVO !")
            p += 1
        else:
            print(">FAUX, la réponse était <",juste,'>',sep='')
        del fr[r]
        del et[r]
    print("\nFin du test ",p,"/",N,sep='')
    input("Appuiez sur entrée pour revenir au menu...")

def controle(list1, list2, list3):
    N = len(list1)
    print("Bienvenue dans le mode CONTROLE\n")
    fr,et = list1[:], list2[:]
    p = 0   #nomre de point pour chaque réponse juste
    corrige = []
    for i in range(N):
        r = randint(0, len(fr)-1)
        if randint(0, 1):
            mot, juste = fr[r], et[r]
            corrige.append(fr[r])
            index = list2.index(juste)
        else:
            mot, juste = et[r], fr[r]
            corrige.append(et[r])
            index = list1.index(juste)
        print(i+1,'/',N,' <',mot, sep='',end='> : ')
        reponse = input()
        if reponse == juste:
            if list3[index] > 0 :
                list3[index] -= 3
                if list3[index] < 0:
                    list3[index] = 0                
            p += 1
            del corrige[-1]
        else:
            list3[index] += 6
            corrige.append(juste)
            if reponse:
                corrige.append(reponse)
            else:
                corrige.append('<vide>')
        del fr[r]
        del et[r]
    print("\nFin du contrôle ",int(p/N*20),'/',20,sep='')
    if p != N:
        reponse =  input("Voulez voir le corrigé ? (Y/n) : ")
        if reponse == 'Y':
            n = int(len(corrige)/3)
            for i in range(n):
                print(i+1,'/',n," La traduction de ",corrige[i*3]," est <",corrige[i*3+1],"> (≠",corrige[i*3+2],")", sep='', end='')
                input()
            print()
    if p == N or reponse == 'Y':
        input("Appuiez sur entrée pour revenir au menu...")

def hard(list1, list2, list3, list4):
    N = len(list1)
    print("Bienvenue dans le mode Point Faible")
    top = [list3[:],[i for i in range(len(list3))]]
    trier = True
    while trier:
        trier = False
        for i in range(len(top[0])-1):
            if top[0][i] < top[0][i+1]:
                trier = True
                for j in range(2):
                    top[j][i], top[j][i+1] = top[j][i+1], top[j][i]
    if top[0].count(0) == len(top[0]):
        print("Félicitation ! Vous n'avez aucune difficultée :) ")
        input("\nAppuyez sur entrée pour revenir au menu...")
    else:
        print("Ce mode analyse vos points faibles\nEt vous premet de vous concentrez sur vos difficultées\n")
        if 0 in top[0]:
            total = top[0].index(0)
        else:
            total = N
        if total > 1:
            print("Tu as",total,"difficultées sur", N, "mots\n")
        n = total
        if n > int(N/2):
            n = 0
            pc = int(input("Quelle quantité en % voulez vous trvailler ? : "))
            n = int(pc * total / 100)
            if n < 1:
                n = 1
        if total == 1:
            print("Tu as une difficultée :")
        else:
            print("Tes mot(s) les plus difficile(s) sont dans l'ordre décroissant : ")
        for i in range(n):
            print('<', list1[top[1][i]],'>(',top[0][i]/10,')',sep='', end='  ')
        motFR = [list1[top[1][i]] for i in range(n)]
        motET = [list2[top[1][i]] for i in range(n)]
        langue = list4
        play = True
        while play:
            print("\n\nQue veux tu faire pour t'améliorer ? ")
            print("1. Apprendre")
            print("2. Reviser")
            print("3. Test")
            print("4. Quitter(Menu)")
            choix = input("Lancer le mode :")
            print()
            if choix == '1':
                apprendre(motFR, motET)
            elif choix == '2':
                reviser(motFR, motET, langue)
            elif choix == '3':
                test(motFR, motET, langue)
            elif choix == '4':
                play = False
            else:
                print("Choix inconnu, erreur...")

def pendu(list1, list2, list3):
    def checkE(mot):
        for i in range(len(mot)):
            if mot[i] == 'é' or mot[i] == 'è':
                e = True

    def affiche():
        for i in range(len(find)):
            if find[i]  == '_':
                print('_',end=' ')
            else:
                print(word[i],end=' ')
        print()
    
    def check(lettre):
        if len(lettre) != 1 and lettre != 'exit':
            print('Erreur...')
            return 0
        for i in range(len(use)):
            if lettre == use[i]:
                print('Vous avez déjà utilisé cette lettre...')
                return 0
        checking = True
        for i in range(len(find)):
            if lettre == word[i]:
                find[i] = lettre
                checking = False
        return checking
    
    def l(ligne, mini, max):
        a = mini
        while a < max:
            pendu[ligne][a] = '#'
            a += 1
    
    def c(colonne, mini, max):
        a = mini
        while a < max:
            pendu[a][colonne] = '#'
            a += 1
    
    def life(vie, affiche):
        if vie == 7:
            l(7, 0, 9)
        elif vie == 6:
            c(3, 2, 7)
        elif vie == 5:
            l(1, 3, 13)
        elif vie == 4:
            pendu[3][4] = '#'
            pendu[2][6] = '#'
        elif vie == 3:
            pendu[2][12] = '|'
        elif vie == 2:
            pendu[3][12] = '0'
        elif vie == 1:
            c(12, 4, 7)
        elif vie == 0:
            l(4, 10, 15)
        if affiche == True:
            for i in range(8):
                for j in range(17):
                    print(pendu[i][j],end='')
                print()

    def end(mot):
        for i in range(len(mot)):
            if mot[i] == '_':
                return 0
        return 1

   
    #programme principal
    vie = 8
    gagner = False  
    e = False   
    use = []    
    pendu = []
    print("Bienvenue dans le jeux du PENDU\n")
    print("Vous voulez jouer en ",list3[0],'(1)/',list3[1],"(2) : ",sep='',end='')
    langue = input()
    if langue == '1':
        word = list1[randint(0,len(list1)-1)]       
    else:
        word = list2[randint(0,len(list2)-1)]
    find = ['_']*len(word)
    find[0] = word[0]
    checkE(word)
    #pendu graphique
    for i in range(8):
        pendu.append([' ']*17)
    #boucle du jeux
    while vie > 0 and gagner == False: 
        affiche()
        r = input("Entrez une lettre : ")
        if check(r) == True:
            vie -= 1
            use.append(r)
        if e == True and r == 'e':  
            check('é')
            check('è')
        if r == 'exit':
            for i in range(vie):
                life(vie, False)
                vie -= 1
        life(vie, True)
        gagner = end(find)
    if vie == 0:
        print('\nPERDU\nLe mot était <',word,'>', sep='')
    else:           
        affiche()
        print('\nBRAVO ! ^^')
    input("\nFin du jeu pendu\nAppuiez sur entrée pour revenir au menu...")

def init():
    f = open("mot.txt", 'r', encoding='Utf-8')
    langue = ['']*2
    list1 = []
    list2 = []
    list3 = []
    tout = []
    read = f.readline()
    langue[0], langue[1] = read[1:3], read[4:6]
    read = f.readline()
    while read != '\n':
        tout.append(read)
        read = f.readline()
    """
    def sep(mot, str):
        temp = ''
        c += 1
        while mot[c] != str:
            temp += mot[c]
            c += 1
        return temp
    
    for mot in tout:
        c = -1
        list1.append(sep(mot, '='))
        list2.append(sep(mot, '.'))
        list3.append(sep(mot, '\n'))
    """
    for mot in tout:
        temp = ''
        c = 0
        while mot[c] != '=':
            temp += mot[c]
            c += 1
        list1.append(temp)
        temp = ''
        c+=1
        while mot[c] != '.':
            temp += mot[c]
            c += 1
        list2.append(temp)
        temp = ''
        c+=1
        while mot[c] != '\n':
            temp += mot[c]
            c += 1
        list3.append(temp)
    list3 = [int(i[1:len(i)-1])*10 for i in list3]
    f.close()

    return list1, list2, langue, list3

def save(list1, list2, list3, list4):
    #Cette fonction arrondie() sert à renvoyer un arrondie d'un float à une decimal uniquement 
    #car la fonction round() return, si la décimal = 5, l'arrondie supérieur si le float est impaire
    #et inférieur si le float est paire
    #c'est à dire : 
    #Python 3.7.4 (Jul 8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
    #>>>round(3.5) --> 4
    #>>>roud(2.5) --> 2
    #Ce qui est problématique..
    def arrondie(float):
        dec = int(str(int(float*10))[-1])
        if dec < 5:
            return int(float)
        else:
            return int(float)+1
    f = open("mot.txt", 'r', encoding='Utf-8')
    for l in f:
        if l == '\n':
            break
    save = f.readlines()
    f.close()
    f = open("mot.txt", 'w', encoding='Utf-8')
    f.write('['+list4[0]+'='+list4[1]+']\n')
    for i in range(len(list1)):
        f.write(list1[i]+'='+list2[i]+'.('+str(arrondie((list3[i]+1)/10))+')\n')
    f.write('\n')
    for index in save:
        f.write(index)
    f.close()


#programme principal
from random import randint
print("Bienvenue dans <LE Boss En Langue> !")
motFR, motET, langue, pointF = init()
play = True
while play:
    print("\n####### MENU ########")
    print("## 1. Apprendre    ##")
    print("## 2. Reviser      ##")
    print("## 3. Test         ##")
    print("## 4. Contrôle     ##")
    print("## 5. Point faible ##")
    print("## 6. Pendu        ##")
    print("## 7. Quitter      ##")
    print("#####################")
    choix = input("Lancer le mode : ")
    print()
    if choix == '1':
        apprendre(motFR, motET)
    elif choix == '2':
        reviser(motFR, motET, langue)
    elif choix == '3':
        test(motFR, motET, langue)
    elif choix == '4':
        controle(motFR, motET, pointF)
    elif choix == '5':
        hard(motFR, motET, pointF, langue)
    elif choix == '6':
        pendu(motFR, motET, langue)
    elif choix == '7':
        play = False
    else:
        print("Choix inconnu, erreur...")
print("A bientôt !")
save(motFR, motET, pointF, langue)
