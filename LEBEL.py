# Ce programme est la v1.0 du projet LEBEL
# fait le 19/10/19, par Alexandre BADER

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

#programme principal
from random import randint
motFR = ['bonjour', 'chat', 'aujourd\'hui', 'demain', 'chien']
motEN = ['hello', 'cat', 'today', 'tomorrow', 'dog']
langue = ['fr', 'en']
N = len(motFR)
play = True
while play:
    print("    MENU")
    print("1. Apprendre")
    print("2. Reviser")
    print("3. Test")
    print("4. Quitter")
    try :
        choix = int(input("Lancer le mode : "))
    except:
        choix = 0
        input("Désoler je n'ai pas compris")
    print()
    if choix == 1:
        apprendre(motFR, motEN)
    elif choix == 2:
        reviser(motFR, motEN, langue)
    elif choix == 3:
        test(motFR, motEN, langue)
    elif choix == 4:
        play = 0
print("\nA bientôt !")