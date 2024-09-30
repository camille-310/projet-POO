#!/bin/env python3
import sys, re


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
                if i!=2:                             # pour la premiÃ¨re liste, on ne fait rien
                    l.append(_construire())
            elif sys.argv[i]=="]":                   # c'est la fin de la liste,
                i+=1
                return l                             # on renvoie la liste constuite
            else:                                    # c'est une liste d'entiers
                l.append(int(sys.argv[i]))
                i+=1
    i = 1                                            # indice pour parcourir les arguments
    return _construire()

def build(l0):
    """
    Cette fonction construit la liste correspondant Ã  sa reprÃ©sentation chaine de caractÃ¨re fourni en argument.
    """

    def _build():
        nonlocal i
        l = []                                       # sous-liste courante
        while True:
            if l0[i]=="[":                           # c'est une sous-liste de listes
                i+=1
                if i!=1:                             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(_build())               # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]":                         # c'est la fin de la sous-liste courante,
                i+=1
                return l                             # on renvoie la sous-liste courante
            else:                                    # c'est une sous-liste d'entiers
                l.append(int(l0[i]))
                i+=1
    i = 0
    res = _build()
    return res

def mklist(lline):

    global i
    l = []                                          # liste courante
    while True:
        if lline[i]=="[":                           # c'est une liste de listes
            i+=1                                    # argument suivant
            if i!=1:                                # pour la premiÃ¨re liste, on ne fait rien
                l.append(mklist(lline))             # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]":                         # c'est la fin de la liste,
            i+=1
            return l                                # on renvoie la liste courante
        else:                                       # c'est une liste d'entiers
            l.append(int(lline[i]))
            i+=1

def module():

    global i
    L = []

    if len(sys.argv)>2:
        # programme principal (liste rentrée en argument)
        l = construire()
        L.append(l)                                # rÃ©cupÃ©ration de la liste
        return L

    elif len(sys.argv)==1:
        # programme principal (liste rentrée par l'utilisateur)
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i = 0
            l = mklist(lline)                      # rÃ©cupÃ©ration de la liste
            L.append(l)
            return L

    else :
        # programme principal (liste tirée d'un fichier)
        f = open(sys.argv[1], "r")
        for line in f:
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)
            L.append(l)
        return L
