#!/bin/env python3
import sys

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.

    Ce programme est appelÃ© avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit Ãªtre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

def construire():
    def _construire():
        """
        Cette fonction rÃ©cursive construit la liste
        Ã  partir des arguments fournis sur la ligne de commande.
        Elle retourne la liste construite.
        """

        nonlocal i
        l = []
        while True:
            if sys.argv[i]=="[":
                i+=1
                if i!=2:                  # pour la premiÃ¨re liste, on ne fait rien
                    l.append(_construire())
            elif sys.argv[i]=="]":        # c'est la fin de la liste,
                i+=1
                return l                  # on renvoie la liste constuite
            else:                         # c'est une liste d'entiers
                l.append(int(sys.argv[i]))
                i+=1
    i = 1                              # indice pour parcourir les arguments
    return _construire()

def minmax(l):
    """
    Cette fonction rÃ©cursive retourne le minmax de la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    # programme principal
    l = construire()                   # rÃ©cupÃ©ration de la liste
    maxi = []
    minmax(l)
    print(min(maxi))
