# Ce programme est la v2.1 du projet LEBEL
# fait le 21/10/19, par Alexandre BADER

def apprendre(list1, list2):
    global N
    print("Bienvenue dans le mode APPRENDRE\n")
    for i in range(N):
        print(i+1,'. ', list1[i],' = ', list2[i],sep='',end=' ')
        input()
    input("\nFin de l'apprentissage\nAppuiez sur entrée pour revenir au menu...")

def reviser(list1, list2, list3):
    global N
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
    global N
    p = 0
    print("Bienvenue dans le mode TEST\n")
    print("Vous voulez réviser en ",list3[0],'(1)/',list3[1],"(2) : ",sep='',end='')
    langue = input()
    fr,et = list1[:], list2[:]
    for i in range(N):
        r = randint(0, len(fr)-1)
        print("Donne moi la traduction de <",end='')
        if langue == '1':
            print(fr[r],'> : ',sep='',end='')
            juste = et[r]
        else:
            print(et[r],'> : ',sep='',end ='')
            juste = fr[r]
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

def controle(list1, list2):
    global N
    print("Bienvenue dans le mode contrôle\n")
    fr,et = list1[:], list2[:]
    p = 0
    corrige = []
    for i in range(N):
        r = randint(0, len(fr)-1)
        if randint(0, 1):
            print(i+1,'/',N,' <',fr[r], sep='',end='> : ')
            juste = et[r]
            corrige.append(fr[r])
        else:
            print(i+1,'/',N,' <',et[r], sep='',end='> : ')
            juste = fr[r]
            corrige.append(et[r])
        reponse = input()
        if reponse == juste:
            p += 1
            del corrige[-1]
        else:
            corrige.append(juste)
            if reponse == '':
                corrige.append('<vide>')
            else:
                corrige.append(reponse)
        del fr[r]
        del et[r]
    print("\nFin du contrôle ",int(p/N*20),'/',20,sep='')
    if p != N:
        reponse =  input("Voulez voir le corrigé ? (Y/n) : ")
        if reponse == 'Y':
            for i in range(int(len(corrige)/3)):
                print("La traduction de ",corrige[i*3]," est <",corrige[i*3+1],"> (≠",corrige[i*3+2],")", sep='', end='')
                input()
            print()
    if p == N or reponse == 'Y':
        input("Appuiez sur entrée pour revenir au menu...")

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
        if len(lettre) != 1:
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
    def life(vie):
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
        for i in range(8):
            for j in range(17):
                print(pendu[i][j],end='')
            print()

    def end(mot):
        for i in range(len(mot)):
            if mot[i] == '_':
                return 0
        return 1
        
    #debut du programme
    vie = 8
    gg = False  
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
    checkE(word)
    #pendu graphique
    for i in range(8):
        pendu.append([' ']*17)
    r = ''
    #boucle du jeux
    while vie > 0 and gg == False and r !='exit': 
        affiche()
        r = input("Entrez une lettre : ")
        if check(r) == True:
            vie -= 1
            use.append(r)
        if e == True and r == 'e':  
            check('é')
            check('è')
        life(vie)
        gg = end(find)
    if vie == 0 or r == 'exit':    
        print('\nPERDU\nLe mot était',word)
    else:           
        affiche()
        print('\nBRAVO ! ^^')
    input("Appuiez sur entrée pour revenir au menu...")

def fichier():
    f = open("mot.old.txt", 'r', encoding='Utf-8')
    langue = ['']*2
    list1 = []
    list2 = []
    tout = []
    read = f.readline()
    langue[0], langue[1] = read[1:3], read[4:6]
    read = f.readline()
    while read != '\n':
        read = read[0:len(read)-1]
        tout.append(read)
        read = f.readline()
    for mot in tout:
        temp2 = ''
        c = 0
        while mot[c] != '=':
            temp2 += mot[c]
            c += 1
        list1.append(temp2)
        temp2 = ''
        c+=1
        while c != len(mot):
            temp2 += mot[c]
            c += 1
        list2.append(temp2)
    f.close()
    return list1, list2, langue, len(list1)

#programme principal
from random import randint
motFR, motET, langue, N = fichier() 
play = True
print("Bienvenue dans <LE Boss En Langue> !")
while play:
    print("\n####### MENU ######")
    print("## 1. Apprendre  ##")
    print("## 2. Reviser    ##")
    print("## 3. Test       ##")
    print("## 4. Contrôle   ##")
    print("## 5. Pendu      ##")
    print("## 6. Quitter    ##")
    print("###################")
    choix = input("Lancer le mode : ")
    print()
    if choix == '1':
        apprendre(motFR, motET)
    elif choix == '2':
        reviser(motFR, motET, langue)
    elif choix == '3':
        test(motFR, motET, langue)
    elif choix == '4':
        controle(motFR, motET)
    elif choix == '5':
        pendu(motFR, motET, langue)
    elif choix == '6':
        play = False
    else:
        print("Choix inconnu, erreur...")
print("A bientôt !")
