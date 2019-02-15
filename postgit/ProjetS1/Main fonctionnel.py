
# ==============================================================================
# LECTURE_PERSONNAGE : lit les personnages dans un fichier et renvoie un
# tableau de personnage. Chaque personnage est lui même contenu dans un tableau
# à importer dans votre programme : import lecture_personnage
# ==============================================================================
from random import *

def lecture_personnages(nom_fichier) :
    """ lit les personnages dans un fichier et renvoie un tableau de personnage.
        Chaque personnage est lui même contenu dans un tableau """
    assert isinstance(nom_fichier, str), "Type nom_fichier incorrect, il faut un str"
    
    #var
    texte,carac = "",""     # str
    tab_perso,perso = [],[] # list

    #begin
    try:
        fichier = open(nom_fichier,'r')
    except IOError:
        print(nom_fichier,": fichier inconnu")
        return []
      
    texte = fichier.read().strip() # lit le fichier en entier et supprime les caractères parasites
    fichier.close()

    try:
        # convertit la chaine de caractères en tableau de tableau de chaines de caractères
        tab_perso=[perso.split(";") for perso in texte.split('\n')]

        # supprime la première ligne avec les titres
        tab_perso=tab_perso[1:]  

        # convertit chaque chaine numérique en entier, mais conserve le nom tel quel
        tab_perso=[[perso[i] if i == 0 else int(perso[i]) for i in range(len(perso))] for perso in tab_perso]
    except ValueError:
        print(nom_fichier,": fichier mal formé")
        return []
        
    return tab_perso
    #end

def dé(nombre_faces) :
    résultat = randint(1,nombre_faces)
    return résultat

class personnage(object):
    def _init_s(self):
        self.nom = ""
        self.force = 0
        self.point_de_vie = 0
        self.classe_armure = 0
        self.bonus_init = 0
        self.base_atk = 0
        self.type_arme = 0
        self.nombre_dés = 0
        self.type_dés = 0
        self.zone_crit = 0
        self.facteur_crit = 0
        self.magic_bonus = 0
        self.potions_légères = 0
        self.potions_modérées = 0
        self.potions_importantes = 0
        self.équipe = ""
        
        


def initialise_perso(tab_perso):
    #assert isinstance(tab_perso,list), "votre message d'erreur"

    #var
    aya = personnage()

    #begin
    perso.nom = tab_perso[0]
    perso.force = tab_perso[1]
    perso.point_de_vie = tab_perso[2]
    perso.classe_armure = tab_perso[3]
    perso.bonus_init = tab_perso[4]
    perso.base_atk = tab_perso[5]
    perso.type_arme = tab_perso[6]
    perso.nombre_dés = tab_perso[7]
    perso.type_dés = tab_perso[8]
    perso.zone_crit = tab_perso[9]
    perso.facteur_crit = tab_perso[10]
    perso.magic_bonus = tab_perso[11]
    perso.potions_légères = tab_perso[12]
    perso.potions_modérées = tab_perso[13]
    perso.potions_importantes = tab_perso[14]
    perso.équipe = tab_perso[15]
    
    

    return aya

"""def initialise_equipe(Tableau_général):
    #on recoit un tableau de personnage eux-meme sous forme de tableau

    #var
    for i in Tableau_général :
        tab_perso=Tableau_général[i]
    tab_perso=[personnage() for i in range(len(Tableau_général))]
    # ona un tableau de personnages

    #begin
    for i in range(len(Tableau_général)):
        tab_perso[i] = initialise_perso(Tableau_général)[i]

    return tab_perso"""

def triSelection (a):
    n = len(a)
    for i in range (n) :
        k = i
        for j in range (i+1,n) :
            if a[k]>a[j] :
                k=j
        a[k],a[i]=a[i],a[k]

def décision():
    décision = input("Quelle action voulez-vous réaliser, 'Attaquer' ou 'Soigner' ?",)
    if décision == "Attaquer" :
        return True
    elif décision == "Soigner" :
        return False






def atk(acteur,Tableau_général,blueteam,redteam):
    base_atk=acteur[5]
    type_arme=acteur[6]
    nombre_dés_dégâts=acteur[7]
    type_dés_dégâts=acteur[8]
    zone_crit=acteur[9]
    facteur_crit=acteur[10]
    magic_bonus=acteur[11]
    
    if acteur[15]=="Blue":
        att=input("Les personnages que vous pouvez attaquer sont Gromel, Stings, Tytharas et Orvis,lequel souhaitez-vous attaquer ?",)
        if "Gromel"==att:
            victime = Tableau_général[4]
            classe_armure_adversaire = victime[3]
            dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
            victime[2] = victime[2] - dégâts_effectifs
            print("Voici les PV de votre cible après l'attaque",victime[2])
            return(1)
        if "Stings"==att :
            print("oui")
            victime = Tableau_général[5]
            print(victime)
            classe_armure_adversaire = victime[3]
            dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
            victime[2] = victime[2] - dégâts_effectifs
            print("Voici les PV de votre cible après l'attaque",victime[2])
            return(1)
        if "Tytharas"==att :
            victime = Tableau_général[6]
            classe_armure_adversaire = victime[3]
            dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
            victime[2] = victime[2] - dégâts_effectifs
            print("Voici les PV de votre cible après l'attaque",victime[2])
            return(1)
        if "orvis"==att :
            victime = Tableau_général[7]
            classe_armure_adversaire = victime[3]
            dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
            victime[2] = victime[2] - dégâts_effectifs
            print("Voici les PV de votre cible après l'attaque",victime[2])
            return(1)
        
    elif acteur[15]=="Red":
        att=input("Les personnages que vous pouvez attaquer sont Leto, Duncan, Feyd et Alia,lequel souhaitez-vous attaquer ?",)
        print(att)
        if "Feyd"==att:
                victime = Tableau_général[0]
                classe_armure_adversaire = victime[3]
                dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
                victime[2] = victime[2] - dégâts_effectifs
                print("Voici les PV de votre cible après l'attaque",victime[2])
                return(1)
        if "Leto"==att :
                victime = Tableau_général[1]
                print("LetoVictime")
                classe_armure = Tableau_général[1][3]
                dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure,facteur_crit)
                victime[2] = victime[2] - dégâts_effectifs
                print("Voici les PV de votre cible après l'attaque",victime[2])
                return(1)
        if "Duncan"==att :
                victime = Tableau_général[2]
                classe_armure_adversaire = victime[3]
                dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
                victime[2] = victime[2] - dégâts_effectifs
                print("Voici les PV de votre cible après l'attaque",victime[2])
                return(1)
        if "Alia"==att :
                victime = Tableau_général[3]
                classe_armure_adversaire = victime[3]
                dégâts_effectifs = attaque(base_atk,nombre_dés_dégâts,type_dés_dégâts,magic_bonus,classe_armure_adversaire,facteur_crit)
                victime[2] = victime[2] - dégâts_effectifs
                print("Voici les PV de votre cible après l'attaque",victime[2])
                return(1)
def soin_including_test_PV_max(personnage, valeur_soin):
    if personnage[3]+valeur_soin > PV_max :
        personnage[3]=PV_max
    else :
        personnage[3]=personnage[3]+PV_max

def soin(potions_légères,potions_modérées,potions_importantes) :
    if potions_légères or potions_modérées or potions_importantes > 0:
        if n_potions_légères > 0 :
            if n_portions_modérées > 0 :
                if n_potions_importantes > 0 :
                    potion_utilisée = input("Il vous reste",n_potions_légères,"potions légères,",n_potions_modérées,"potions modérées et",n_potions_importantes,"potions importantes, laquelle souhaitez-vous utiliser ?")
                    if potion_utilisée == "Une potion légère" :
                        valeur_soin = dé(8)+1
                        soin_including_test_PV_max(personnage, valeur_soin)
                    elif potion_utilisée == "Une potion modérée" :
                        valeur_soin = dé(8)+dé(8)+3
                        soin_including_test_PV_max(personnage, valeur_soin)
                    elif potion_utilisée == "Une potion importante" :
                        valeur_soin = dé(8)+dé(8)+dé(8)+5
                        soin_including_test_PV_max(personnage, valeur_soin)
                else :
                    potion_utilisée = input("Il vous reste",n_potions_légères,"potions légères et",n_potions_modérées,"potions modérées, laquelle souhaitez_vous utiliser ?")
                    if potion_utilisée == "Une potion légère" :
                        valeur_soin = dé(8)+1
                        soin_including_test_PV_max(personnage, valeur_soin)
                    elif potion_utilisée == "Une potion modérée" :
                        valeur_soin = dé(8)+dé(8)+3
                        soin_including_test_PV_max(personnage, valeur_soin)
            else :
                potion_utilisée = input("Il vous reste uniquement",n_potions_légères)
                valeur_soin = dé(8)+1
                soin_including_test_PV_max(personnage, valeur_soin)
    else :
        print("Vous n'avez plus de potions vous ne pouvez plus soignez")


def heal(acteur) :
    potions_légères=acteur[12]
    potions_modérées=acteur[13]
    potions_importantes=acteur[14]
    PV_max=acteur[16]
    valeur_soin = soin(potions_légères,potions_modérées,potions_importantes)
    soin_including_test_PV_max(acteur, valeur_soin)
    print("Vous vous êtes soigné de",soin_including_test_PV_max)
    return(1)
    
def main():

    ############DEF TABLEAU#############
    #Défintion premier tableau plus ajout d'une variable définissant l'équipe
    Tableau_équipe1=(lecture_personnages("Tableau1.csv"))
    Tableau_équipe1[0].append("Red")
    Tableau_équipe1[0].append(Tableau_équipe1[0][2]) #Ajout case PV MAX nécessaire pour les soins
    Tableau_équipe1[1].append("Red")
    Tableau_équipe1[1].append(Tableau_équipe1[1][2])
    Tableau_équipe1[2].append("Red")
    Tableau_équipe1[2].append(Tableau_équipe1[2][2])
    Tableau_équipe1[3].append("Red")
    Tableau_équipe1[3].append(Tableau_équipe1[3][2])
    #Définition second tableau plus ajout d'une variable définissant l'équipe"""
    Tableau_équipe2=(lecture_personnages("Tableau1.csv"))
    Tableau_équipe2[0].append("Blue")
    Tableau_équipe2[0][0]="Feyd" #renommage pour clarté pour utilisateur
    Tableau_équipe2[0].append(Tableau_équipe1[0][2])
    Tableau_équipe2[1].append("Blue")
    Tableau_équipe2[1][0]="Leto"        #idem
    Tableau_équipe2[1].append(Tableau_équipe1[1][2])
    Tableau_équipe2[2].append("Blue")
    Tableau_équipe2[2][0]="Duncan"      #idem
    Tableau_équipe2[2].append(Tableau_équipe1[2][2])
    Tableau_équipe2[3].append("Blue")
    Tableau_équipe2[3][0]="Alia"        #idem
    Tableau_équipe2[3].append(Tableau_équipe1[3][2])
    #Définition tableau général comme une réunion des deux tableaux précédents
    Tableau_équipe1=[Tableau_équipe1[0],Tableau_équipe1[1],Tableau_équipe1[2],Tableau_équipe1[3]] #pour que les append soient pris en compte 
    Tableau_équipe2=[Tableau_équipe2[0],Tableau_équipe2[1],Tableau_équipe2[2],Tableau_équipe2[3]] #idem
    Tableau_général = [Tableau_équipe1[0],Tableau_équipe1[1],Tableau_équipe1[2],Tableau_équipe1[3],Tableau_équipe2[0],Tableau_équipe2[1],Tableau_équipe2[2],Tableau_équipe2[3]]
    #Définition ensembles d'équipe
    blueteam = [Tableau_général[4],Tableau_général[5],Tableau_général[6],Tableau_général[7]]
    redteam = [Tableau_général[0],Tableau_général[1],Tableau_général[2],Tableau_général[3]]
    
    #print(Tableau_équipe2)
     ########### INITIATIVE #############
    a = dé(20) + Tableau_général[0][4] #calcul d'initiative avec chaque bonus d'attribué 
    b = dé(20) + Tableau_général[1][4]
    c = dé(20) + Tableau_général[2][4]
    d = dé(20) + Tableau_général[3][4]
    e = dé(20) + Tableau_général[4][4]
    f = dé(20) + Tableau_général[5][4]
    g = dé(20) + Tableau_général[6][4]
    h = dé(20) + Tableau_général[7][4]
    Tableau_général[0].append(a)        #ajout d'une case iniative dans les personnages et attribution de celle-ci
    Tableau_général[1].append(b)
    Tableau_général[2].append(c)
    Tableau_général[3].append(d)
    Tableau_général[4].append(e)
    Tableau_général[5].append(f)
    Tableau_général[6].append(g)
    Tableau_général[7].append(h)
    print(Tableau_général)
    ####################################

    taborder0=[Tableau_général[0][17],Tableau_général[0][0]]    #Puisque 16 = vie max, puisque défini auparavant
    taborder1=[Tableau_général[1][17],Tableau_général[1][0]]
    taborder2=[Tableau_général[2][17],Tableau_général[2][0]]
    taborder3=[Tableau_général[3][17],Tableau_général[3][0]]
    taborder4=[Tableau_général[4][17],Tableau_général[4][0]]
    taborder5=[Tableau_général[5][17],Tableau_général[5][0]]
    taborder6=[Tableau_général[6][17],Tableau_général[6][0]]
    taborder7=[Tableau_général[7][17],Tableau_général[7][0]]
    Tableau_ordre=[taborder0,taborder1,taborder2,taborder3,taborder4,taborder5,taborder6,taborder7]
    #print(Tableau_ordre)
    #print(max(Tableau_ordre))

    personnage = (max(Tableau_ordre))[1]
    str(personnage)
    print(personnage)
    personnage = "Gromel"
    i = 5
    "for i in range(len(Tableau_général)) :"
    if i == 5 :
        if Tableau_général[0][0]==personnage :
                acteur = Tableau_général[0]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)                
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40

        if Tableau_général[1][0]==personnage :
                acteur = Tableau_général[1]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)        
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
                
        if Tableau_général[2][0]==personnage :
                acteur = Tableau_général[2]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)               
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
                
        if Tableau_général[3][0]==personnage :
                acteur = Tableau_général[3]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)               
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
                
        if Tableau_général[4][0]==personnage :
                acteur = Tableau_général[4]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
                
        if Tableau_général[5][0]==personnage :
                acteur = Tableau_général[5]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
                
        if Tableau_général[6][0]==personnage :
                acteur = Tableau_général[6]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40

        if Tableau_général[7][0]==personnage :
                acteur = Tableau_général[7]
                print("Le personnage agissant ce tour ci est",Tableau_général[0][0])
                if décision()==True :
                    atk(acteur,Tableau_général,blueteam,redteam)
                elif décision()==False :
                    soin(acteur)
                acteur[17]=acteur[17]-40
            

    

    
    

    





if __name__ == "__main__" :
    main()

    
# ==============================================================================
