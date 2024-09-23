#!/bin/env python3
import sys, Module


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
    l = Module.module()
    maxi = []
    minmax(l)
    print(min(maxi))
