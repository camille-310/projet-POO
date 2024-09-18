#!/bin/env python3
import sys, re

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.

    Ce programme lit des liste de type L sur l'entrÃ©e standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triÃ©es.
"""

def tri(l):
    """
    Cette fonction rÃ©cursive tri la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

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

def build(l0):
    """
    Cette fonction construit la liste correspondant Ã  sa reprÃ©sentation chaine de caractÃ¨re fourni en argument.
    """

    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))
                i+=1
    i = 0
    res = _build()
    return res

def mklist():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la premiÃ¨re liste, on ne fait rien
                l.append(mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))
            i+=1

if __name__=="__main__":

    if len(sys.argv)>2:
        # programme principal (liste rentrée en argument)
        l = construire()                   # rÃ©cupÃ©ration de la liste
        tri(l)
        print(f"{l=}")

    elif len(sys.argv)==1:
        # programme principal (liste rentrée par l'utilisateur)
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i = 0
            l = mklist()                      # rÃ©cupÃ©ration de la liste
            tri(l)
            print(f"{l=}")

    else :
        # programme principal (liste tirée d'un fichier)
        f = open(sys.argv[1], "r")
        for line in f:
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)
            print(f"{l=}")
            print(f"{tri(l)=}")
