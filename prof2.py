#!/bin/env python3
import sys, re, Module

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passÃ©e en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

if __name__=="__main__":
    # programme principal
    l = Module.module()
    print(f"{l=}")
    print(f"{profondeur(l)=}")
