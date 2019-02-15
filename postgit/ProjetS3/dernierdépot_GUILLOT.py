from ezTK import *





lundi=dict()        #on définit ici nos structures de données avant les fonctions
lundi["0"]="libre"
lundi["1"]="libre"
lundi["2"]="libre"
lundi["3"]="libre"
lundi["4"]="libre"

mardi=dict()            
mardi["0"]="libre"
mardi["1"]="libre"
mardi["2"]="libre"
mardi["3"]="libre"
mardi["4"]="libre"

mercredi=dict()
mercredi["0"]="libre"
mercredi["1"]="libre"
mercredi["2"]="libre"
mercredi["3"]="libre"
mercredi["4"]="libre"

jeudi=dict()
jeudi["0"]="libre"
jeudi["1"]="libre"
jeudi["2"]="libre"
jeudi["3"]="libre"
jeudi["4"]="libre"

vendredi=dict()
vendredi["0"]="libre"
vendredi["1"]="libre"
vendredi["2"]="libre"
vendredi["3"]="libre"
vendredi["4"]="libre"

planning_test=(lundi,mardi,mercredi,jeudi,vendredi)
liste_type_planning=list()
liste_de_base=(type_entité,info_nécessaire1,info_nécessaire2,lundi, mardi, mercredi, jeudi, vendredi)

liste_groupe
dico_groupes=dict()
dico_enseignants=dict()
dico_salles=dict()


def couple_libre_1planning(planning,date,créneau): #test si un craneau à une date est libre
    date_travail=0
    #begin
    if date == "lundi" :
        date_travail=planning[3]
        if date_travail[créneau] in planning == "libre" :
            print("Le créneau" créneau "à la date" date "est libre")
            return 1
        else :
            return 0
    if date == "mardi" :
        date_travail=planning[4]
        if date_travail[créneau] in planning == "libre" :
            print("Le créneau" créneau "à la date" date "est libre")
            return 1
         else :
            return 0
    if date == "mercredi" :
        date_travail=planning[5]
        if date_travail[créneau] in planning == "libre" :
            print("Le créneau" créneau "à la date" date "est libre")
            return 1
        else :
            return 0
    if date == "jeudi" :
        date_travail=planning[6]
        if date_travail[créneau] in planning == "libre" :
            print("Le créneau" créneau "à la date" date "est libre")
            return 1
        else :
            return 0
    if date == "vendredi" :
        date_travail=planning[7]
        if date_travail[créneau] in planning == "libre" :
            print("Le créneau" créneau "à la date" date "est libre")
            return 1
        else :
            return 0
      #end


        
def couple1_application(planning):                  #permet d'input la date et le creneau qu'on teste
    #begin-input
    date=input("Entrez un jour :")
    créneau=input("Entrez un créneau :")
    return (couple_libre_1planning(planning,date,créneau))
    #end
    


def couple_libre_2planning(planning1, planning2):  #teste un couple date heure dans deux plannings 
    #input
    date=input("Entrez un jour :")
    créneau=input("Entrez un créneau :")
    #begin
    if couple_libre_1planning(planning1,date,créneau)==couple_libre_1planning(planning2,date,créneau)==1:
        print("Le créneau" créneau "à la date" date "est libre dans les deux plannings")
        return 1
    else :
        return 0
    #end

def verif_totale(planning_prof, planning_groupe, planning_salle) :
    #input
    date=input("Entrez un jour :")
    créneau=input("Entrez un créneau :")
    #begin
    if planning_prof[0]=="enseignant" :             #test des types des entités des plannings
        if planning_groupe[0]=="groupe" :
            if planning_salle[0]=="salle" :
                if couple_libre_2planning(planning1, planning2) == couple_libre_2planning(planning2, planning3) == 1 :
                    print("Le créneau" créneau "à la date" date "est libre pour l'enseignant, la salle et le groupe d'élèves")
                    return 1
                else :
                    print("Le créneau" créneau "à la date" date "n'est pas valable")
                    return 0
            else :
                print("Il faut rentrer le planning d'une salle")
                return 0
        else :
            print("Il faut rentrer le planning d'un groupe")
            return 0
    else :
        print("Il faut rentrer le planning d'un enseignant")
        return 0

def ajouter_cours(date, créneau, planning_prof, planning_groupe, planning_salle) :
    if verif_totale(planning_prof, planning_groupe, planning_salle)==1 :
        for j in
        if date == "lundi" :
            for i in lundi[i] :
                if i == créneau :
                    lundi[i] = "COURS"
        elif date == "mardi" :
            for i in mardi[i] :
                if i == créneau :
                    mardi[i] = "COURS"
        elif date == "mercredi" :
            for i in mercredi[i] :
                if i == créneau :
                    mercredi[i] = "COURS"
        elif date == "jeudi" :
            for i in jeudi[i] :
                if i == créneau :
                    jeudi[i] = "COURS"
        elif date == "vendredi" :
            for i in vendredi[i] :
                if i == créneau :
                    vendredi[i] = "COURS"

def grid():         #tentative interface graphique
    #VARIABLES
    rows, cols =5,5 
    value_rowsxcols = rows * cols
    turn = 0
    win = Win(title='GRID', grow=True, flow='E') 
  # ----------------------------------------------------------------------------
    
    #BEGIN
    meta_frame1=Frame(win, flow='S', anchor='W')
    fr0=Frame(meta_frame1, flow='S', anchor='NW')
    Button(fr0, height=1, width=1, text='')
    fr1=Frame(meta_frame1, flow='S', grow=True)
    Label(fr1, text='8-10')
    Label(fr1, text='10-12')
    Label(fr1, text='13-15')
    Label(fr1, text='15-17')
    Label(fr1, text='17-19')
    meta_frame2=Frame(win, flow=
                      
    fr2=Frame(win, flow='ES', grow=True, fold=5)
    Label(fr2, text='Lundi')
    Label(fr2, text='Mardi')
    Label(fr2, text='Mercredi')
    Label(fr2, text='Jeudi')
    Label(fr2, text='Vendredi')
    for loop in range(rows*cols):
        Label(fr2, height=6, width=6, bg='#C0C0C0')
    #END

        
        




def main():
    grid()              
    couple1_application(planning_test)
