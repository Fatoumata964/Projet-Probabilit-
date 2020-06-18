import string
import urllib.request
import sys


x = urllib.request.urlopen('https://r-stat-sc-donnees.github.io/LesMiserables1.txt')
str1=str(x.read())



punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"] 


def sup_ponct_Maj_divjet():
    print('Supprimons la ponctuation:',punctuation,' les majuscules / minuscules et divisons le texte en jetons individuels (mots)')
    str_with_Maj = str1.translate(str.maketrans("" ,"", string.punctuation))
    return str_with_Maj
sup_ponct_Maj_divjet()

def question():
    print('Vous avez choisi dafficher le texte sans les ponctuations et les majusccules' )
    question=input('Tapez 1 pour afficher le texte sans ponctuations,\
    2 pour afficher le texte sans ponctuations et majuscules \
    3 pour diviser le texte en jetons individuels (mots)')
    if question == '1':
        print('Supprimons la ponctuation:',punctuation)
        str_with_Maj = str1.translate(str.maketrans("" ,"", string.punctuation))
        print(str_with_Maj)
        return str_with_Maj
       

    elif question =='2':
       print('Supprimons la ponctuation:',punctuation,' les majuscules / minuscules et divisons le texte en jetons individuels (mots)')
       str_with_Maj = str1.translate(str.maketrans("" ,"", string.punctuation))
       str_without_Maj=str_with_Maj.lower()
       jeton=str_without_Maj.split()
       print(str_without_Maj)
       
       return str_without_Maj
       
    elif question =='3':
        str_with_Maj = str1.translate(str.maketrans("" ,"", string.punctuation))
        str_without_Maj=str_with_Maj.lower()
        jeton=str_without_Maj.split()
        print(jeton)
        return jeton
    
    return str_with_Maj,str_without_Maj, jeton

def nombre_de_mots():
    str_with_Maj = str1.translate(str.maketrans("" ,"", string.punctuation))
    str_without_Maj=str_with_Maj.lower()
    jeton=str_without_Maj.split()
    
    Nombre_de_un=0
    for i in range(len(jeton)):
        if jeton[i] == "un":
            Nombre_de_un = Nombre_de_un + 1
    Numun=Nombre_de_un

    Nombre_de_et=0    
    for i in range(len(jeton)):     
        if jeton[i] == "et":
            Nombre_de_et = Nombre_de_et + 1
    Numet=Nombre_de_et

    Nombre_de_le=0
    for i in range(len(jeton)):
        if jeton[i] == "le":
            Nombre_de_le = Nombre_de_le + 1
    Numle=Nombre_de_le

    Nombre_de_il=0
    for i in range(len(jeton)):
        if jeton[i] == "il":
            Nombre_de_il = Nombre_de_il + 1
    Numil=Nombre_de_il

    Nombre_de_est=0
    for i in range(len(jeton)):
        if jeton[i] == "et":
            Nombre_de_est = Nombre_de_est + 1
    Numest=Nombre_de_est
    
    print("Le nombre d'utilisation du mot un est:",Numun)
    print("Le nombre d'utilisation du mot et est:",Numet)
    print("Le nombre d'utilisation du mot le est:",Numle)
    print("Le nombre d'utilisation du mot il est:",Numil)
    print("Le nombre d'utilisation du mot est est:",Numest)
    return Numest,Numun,Numet,Numil,Numle


def menu():         #Création d'un menu pour le programme
        print('\t\t-- Théorème cental limite appliqué au traitement de texte \n')
        print('1. Tapez 1 pour afficher le texte initial')
        print('2. Tapez 2 afficher le texte sans les ponctuations et les majuscules divisons le texte en jetons individuels (mots)')
        print('3. Tapez 3 pour afficher le nombre utilisé des mots (un, et, le, il, est)')
        print('4. Quitter')         
        saisie = input()
        saisie = int(saisie)         
        while saisie < 1 or saisie > 4:
                print('Erreur, 1 pour afficher le texte initial,2 pour afficher les condtionnements et 3 pour Quitter')
                saisie = input()
                saisie = int(saisie)         
        if saisie == 2:              
               question()   
        elif saisie ==3:
            nombre_de_mots()
        elif saisie == 1:
                print (str1)      
                menu()
        else:
                return 0
        rejouer()
        
def rejouer(): # Choisir de revenir à une autre question
   print("Veux tu choisir une autre question?!\n")
   while True:
        gameChoice = input("oui pour revenir,non pour quitter\n").lower()
        if gameChoice == "oui" or gameChoice == "o":
            menu()
        elif gameChoice == "non" or gameChoice == "n":
            sys.exit("A bientot")
menu()    
        

        