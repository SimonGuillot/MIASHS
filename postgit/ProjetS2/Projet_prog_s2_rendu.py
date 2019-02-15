from ezTK import *


#idéalement ici on préférerait utiliser une fonction fonctionnant pour toute les colonnes avec en argument
#le numéro du bouton pour exercer la fonction sur telle colonne. Cependant une erreur apparait comme
#quoi l'index serait "out of range" dans une fonction de ezTK lors de mes tentatives, ainsi, j'ai utilisé une fonction
#par colonne
def colonne1():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(0)
        print(turn,"blue")
    elif turn%2==1:
        redturn(0)
        print(turn,"red")

#====================2
def colonne2():
    global colored
    global turn
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(1)
        print(turn,"blue")
    elif turn%2==1:
        redturn(1)
        print(turn,"red")


#===================3
def colonne3():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(2)
        print(turn,"blue")
    elif turn%2==1:
        redturn(2)
        print(turn,"red")


#============================4
def colonne4():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(3)
        print(turn,"blue")
    elif turn%2==1:
        redturn(3)
        print(turn,"red")

#============================5
def colonne5():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(4)
        print(turn,"blue")
    elif turn%2==1:
        redturn(4)
        print(turn,"red")

#==================================6
def colonne6():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(5)
        print(turn,"blue")
    elif turn%2==1:
        redturn(5)
        print(turn,"red")

#===============================7
def colonne7():
    global turn
    global colored
    colored = ['#00F', '#F00']
    if turn%2==0:
        blueturn(6)
        print(turn,"blue")
    elif turn%2==1:
        redturn(6)
        print(turn,"red")
#===============================
def blueturn(value):
    global turn
    i = 6 
    while i > 0:
        if win[i][value]['bg'] in colored :
            i = i - 1
        else :
            win[i][value]['bg'] = '#00F'
            turn = turn + 1
            return turn
        reconnaissance_victoire()
            
def redturn(value):
    global turn
    i = 6
    while i > 0 :
        if win[i][value]['bg'] in colored :
            i = i - 1
        else :
            win[i][value]['bg'] = '#F00'
            i = 0
            turn = turn + 1
            return turn
    reconnaissance_victoire()

def reconnaissance_victoire():
    "red=+1 blue=-1 grey=0 test [0][1-2-3-4], [0][4-5-6-7] value, then [1,2,3...][..]"
    rows, cols = 6,7
    #lettres vertical chiffre horizontal
    i = 6
    j1 = 7
    j2 = 3
    condition_victory_red=0 #on compte avec les variables condition de victoire le nombre de fois où un alignement de 4 apparait
    condition_victory_blue=0
    while i > 0 :
        partial_sum1 = 0  #ces variables partial sum sont en fait les sommes de valeurs de segments de 4 bricks qui servent à tester si il y a alignement ou non
        partial_sum2= 0   # on les déclare dans le while car on ne s'en sert qu'à l'intérieur du while, et on reset les valeurs avant la boucle suivante
        while j1 > j2 :
            if win[i][j1]['bg']=='#F00':
                partial_sum1=partial_sum1+1
                j1=j1-1
            elif win[i][j1]['bg']=='#00F':
                partial_sum1=partial_sum1-1
                j1=j1-1
            elif win[i][j1]['bg']=='#C0C0C0':
                partial_sum1=partial_sum1+0
                j1=j1-1
        if partial_sum1==4 :
            condition_victory_red=condition_victory_red + 1
        elif partial_sum1==-4 :
            condition_victory_blue=condition_victory_blue + 1
        while j2 >= 0 :
            if win[i][j1]['bg']=='#F00':
                partial_sum2=partial_sum2+1
                j2=j2-1
            elif win[i][j1]['bg']=='#00F':
                partial_sum2=partial_sum1-1
                j2=j2-1
            elif win[i][j1]['bg']=='#C0C0C0':
                partial_sum2=partial_sum1+0
                j2=j2-1
        if partial_sum2==4 :
            condition_victory_red=condition_victory_red + 1 #quand les partial sum ont les valeurs significatives de -4 ou 4 qui indiquent un alignement, on rajoute 1 à la variable condition de victoire
        elif partial_sum2==-4 :
            condition_victory_blue=condition_victory_blue + 1
        partial_sum1=0
        partial_sum2=0
        i = i -1
    if condition_victory_blue == 2 : #quand on atteint deux conditions de victoire, un camp a gagné, on l'indique par une fenêtre
        victoire_bleu = Win(master=win, title='Victoire', grow=False)
        text='Les bleu ont gagné'
        Label(victoire_bleu, text=text, fg=fg, bg=bg, width=25, height=2)
    if condition_victory_red == 2 : 
        victoire_rouge = Win(master=win, title='Victoire', grow=False)
        text='Les rouges ont gagné'
        Label(victoire_rouge, text=text, fg=fg, bg=bg, width=25, height=2)
    

def coup_special(player) :
    global count_sp_red, count_sp_blue
    colored = ['#00F', '#F00']
    count_sp_red=1
    count_sp_blue=1
    if player=='red':
        print(count_sp_red)
        if count_sp_red>0 :
            #retournement
            for i in range(0,7):
                if win[i][0]['bg'] in colored :
                    if i == 1 :
                        win[6][0]['bg']=win[i][0]['bg']
                        n=6
                        while n > 0 :
                            if win[n][value]['bg'] in colored :
                                n = n - 1
                            else :
                                win[n][value]['bg'] = '#F00'
                                n = 0
                                
                    elif i == 2:
                        win[5][0]['bg']=win[i][0]['bg']
                        n=5
                        while n > 0 :
                            if win[n][value]['bg'] in colored :
                                n = n - 1
                            else :
                                win[n][value]['bg'] = '#F00'
                                n = 0
                    elif i == 3:
                        win[4][0]['bg']=win[i][0]['bg']
                        n=4
                        while n > 0 :
                            if win[n][value]['bg'] in colored :
                                n = n - 1
                            else :
                                win[n][value]['bg'] = '#F00'
                                n = 0
                    elif i == 4:
                        win[3][0]['bg']=win[i][0]['bg']
                        n=3
                        while n > 0 :
                            if win[n][value]['bg'] in colored :
                                n = n - 1
                            else :
                                win[n][value]['bg'] = '#F00'
                                n = 0
                    elif i == 5:
                        win[2][0]['bg']=win[i][0]['bg']
                        n=2
                        while n > 0 :
                            if win[n][value]['bg'] in colored :
                                n = n - 1
                            else :
                                win[n][value]['bg'] = '#F00'
                                n = 0
                    elif i == 6:
                        win[1][0]['bg']=win[i][0]['bg']

                
            count_sp_red = 0
            print(count_sp_red)
        else :
            #win slave 'vous ne pouvez plus jouer ce coup'
            refus = Win(master=win, title='Impossible', grow=False)
            text='Vous ne pouvez plus jouer ce coup'
            Label(refus, text=text, fg=fg, bg=bg, width=25, height=2)
            count_sp_red = 1
    if player=='blue':
        print(count_sp_red)
        if count_sp_blue>0 :
            #retournement

            count_sp_blue = 0
            print(count_sp_red)
        else :
            #win slave 'vous ne pouvez plus jouer ce coup'
            refus = Win(master=win, title='Impossible', grow=False)
            text='Vous ne pouvez plus jouer ce coup'
            Label(refus, text=text, fg=fg, bg=bg, width=25, height=2)
            count_sp_red = 1


        
            
# ------------------------------------------------------------------------------
def grid():
    global win
    global turn 
    rows, cols =6,7 
    value_rowsxcols = rows * cols
    turn = 0
    win = Win(title='GRID', grow=False, fold=cols, op=2) # create new grid window
  # ----------------------------------------------------------------------------
    Button(win, text='', command=colonne1)
    Button(win, text='', command=colonne2)
    Button(win, text='', command=colonne3)
    Button(win, text='', command=colonne4)
    Button(win, text='', command=colonne5)
    Button(win, text='', command=colonne6)
    Button(win, text='', command=colonne7)
    for loop in range(rows*cols):
        Brick(win, height=64, width=64, bg='#C0C0C0')
    Button(win, text='Coup spécial red', command=coup_special('red'))
    Button(win, text='Coup spécial blue', command=coup_special('blue'))
  # ----------------------------------------------------------------------------
    win.loop()
# ------------------------------------------------------------------------------
def main():
    grid()
# ==============================================================================
if __name__ == "__main__":
    win = None 
    main()
# ==============================================================================


# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================

